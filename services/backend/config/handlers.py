from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView


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
    exception_message = 'The request contains an invalid authentication data'

    def get(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message},
                        status=status.HTTP_403_FORBIDDEN)


class ErrorResponseFactory:
    """
    Factory class to generate custom JSON responses for different exceptions.

    This approach follows the Open/Closed Principle, allowing easy
    extension for new exception types.
    """

    @staticmethod
    def get_error_response(exception, response=None):
        pass

    @staticmethod
    def _build_response(message, error, status_code):
        pass


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
    pass
