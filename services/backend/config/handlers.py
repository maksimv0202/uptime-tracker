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
        return Response({'error': self.exception_message}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message}, status=status.HTTP_400_BAD_REQUEST)


class ExceptionHandler403(APIView):
    exception_message = 'The request contains an invalid authentication data'

    def get(self, request, *args, **kwargs):
        return Response({'error': self.exception_message}, status=status.HTTP_403_FORBIDDEN)

    def post(self, request, *args, **kwargs):
        return Response({'error': self.exception_message}, status=status.HTTP_403_FORBIDDEN)
