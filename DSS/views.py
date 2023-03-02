from rest_framework import generics, serializers
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from DSS.models import Clothes, Person
from DSS.serializers import ClothesSerializer


class ClothesCreateView(generics.CreateAPIView):
    serializer_class = ClothesSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'


class ClothesView(APIView):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Clothes, pk=pk)
        serializer = self.serializer_class(profile)
        return Response({'serializer': serializer, 'profile': profile})


class PersonSerializer(serializers.ModelSerializer):
    recommendation = serializers.CharField(read_only=True, allow_null=True, required=False, label='Рекомендация')

    class Meta:
        model = Person
        fields = '__all__'


class PersonView(APIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'profile_detail.html'

    def get(self, request, pk):
        profile = get_object_or_404(Person, pk=pk)
        profile.__setattr__('name', 'Формирование рекомендаций по подбору одежды ')
        serializer = self.serializer_class(profile)
        return Response({'serializer': serializer, 'profile': profile})

    def post(self, request, pk):
        profile = Clothes.objects.create(**request.data)
        serializer = self.serializer_class(data=request.data, instance=profile)
        serializer.is_valid()
        serializer.save()
        profile.__setattr__('name', 'Формирование рекомендаций по подбору одежды ')
        profile.__setattr__('recommendation', profile.get_recommendation())

        return Response({'serializer': serializer, 'profile': profile})
