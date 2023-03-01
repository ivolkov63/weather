from rest_framework import generics, status
from rest_framework.response import Response

from DSS.models import Clothes
from DSS.serializers import ClothesSerializer


class ClothesCreateView(generics.CreateAPIView):
    serializer_class = ClothesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        recommendation = serializer.instance.give_recommendation()
        serializer.instance.result = recommendation
        serializer.instance.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ClothesView(generics.RetrieveAPIView):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()