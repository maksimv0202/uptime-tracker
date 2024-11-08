from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import (AuthenticationFailed, NotFound,
                                       PermissionDenied, ValidationError)
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler


class ExceptionHandler404(APIView):
    exception_message = 'The requested resource was not found'

    def get(self, request, *args, **kwargs):
        raise NotFound(self.exception_message)

    def post(self, request, *args, **kwargs):
        raise NotFound(self.exception_message)


class ExceptionHandler500(APIView):
    exception_message = 'Internal Server Error'

    def get(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ExceptionHandler400(APIView):
    exception_message = 'Bad Request'

    def get(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_400_BAD_REQUEST)


class ExceptionHandler403(APIView):
    exception_message = 'You do not have permission to access this resource'

    def get(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_403_FORBIDDEN)


class ErrorResponseFactory:
    """
    Factory class to generate custom JSON responses for different exceptions.

    This class uses Python's match/case statements to determine the appropriate error message,
    status code, and error details based on the exception type. It enables consistent and
    structured JSON responses for various common exceptions, such as validation errors,
    authentication errors, permission denials, and resource not found errors.
    """

    @staticmethod
    def get_error_response(exception, response=None):
        match exception:
            case ValidationError():
                return ErrorResponseFactory._build_response(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    error='Validation Error',
                    message=response.data if response else str(exception),
                )
            case NotFound() | Http404():
                return ErrorResponseFactory._build_response(
                    status_code=status.HTTP_404_NOT_FOUND,
                    error='Not Found',
                    message='The requested resource was not found'
                )
            case PermissionDenied():
                return ErrorResponseFactory._build_response(
                    status_code=status.HTTP_403_FORBIDDEN,
                    error='Permission Denied',
                    message='You do not have permission to access this resource'
                )
            case AuthenticationFailed():
                return ErrorResponseFactory._build_response(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    error='Authentication Failed',
                    message='Authentication credentials were not provided or are invalid'
                )
            case _:
                return ErrorResponseFactory._build_response(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    error='Internal Server Error',
                    message='An unexpected error occurred on the server'
                )

    @staticmethod
    def _build_response(status_code, error, message):
        return {
            'status_code': status_code,
            'error': error,
            'message': message
        }, status_code


def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework to ensure
    consistent JSON error responses.

    This handler captures specific exceptions, such as validation errors,
    authentication errors, permission errors, and 404 not found errors,
    and formats them in a JSON response with the fields 'status_code', 'error',
    and 'message'. Unhandled exceptions will return a generic 500 error
    response with a corresponding message.
    """
    response = exception_handler(exc, context)

    if not response:
        custom_response_data, status_code = ErrorResponseFactory.get_error_response(exc)
        return Response(custom_response_data, status=status_code)

    custom_response_data, status_code = ErrorResponseFactory.get_error_response(exc, response)
    response.data = custom_response_data
    response.status_code = status_code

    return response
