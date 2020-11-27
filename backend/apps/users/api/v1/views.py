"""API v1 views"""

# Django rest F.
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

# Serializers
from .serializers import UserSerializer, ChangePasswordSerializer

# Use cases
from .usecases import ChangePasswordUser, CreateNewUser, RaffleResult

# Errors
from .usecases import EmailAlreadyExists


class NewUserView(CreateAPIView):
    """Create new user view"""
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            self._run_use_cases(serializer)
            if not serializer.errors:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _run_use_cases(serializer):
        use_case = CreateNewUser(username=serializer.data['username'], first_name=serializer.data['first_name'],
                                 last_name=serializer.data['last_name'],
                                 email=serializer.data['email'])

        try:
            use_case.execute()
        except EmailAlreadyExists as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordView(CreateAPIView):
    """Change password view"""

    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        """"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            self._run_use_cases(serializer, kwargs['token'])
            if not serializer.errors:
                return Response({'Message': 'Password changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def _run_use_cases(serializer, token):
        """"""
        use_case = ChangePasswordUser(token=token, password=serializer.data['password'])

        try:
            use_case.execute()
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)


class MakeRaffleView(RetrieveAPIView):
    """"""
    serializer_class = UserSerializer
    winner = None

    def get(self, request, *args, **kwargs):
        """"""
        self._run_use_cases()
        serializer = self.serializer_class(instance=self.winner)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def _run_use_cases(self):
        use_case = RaffleResult()
        try:
            self.winner = use_case.make_raffle()
        except Exception as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
