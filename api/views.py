from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializer import DrinkSerializer
from rest_framework.response import Response
from .models import Drinks

@api_view(['GET'])
def apiOverView(request):
    api_urls= {
        'Drinks':'/drinks/',
        'Detailed View':'/drink-details/<str:pk>',
        'Create':'/create-drink',
        'Update':'/update-drink/<str:pk>',
        'Delete':'/delete-drink/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def DrinkList(request):
    drinks = Drinks.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DrinkDetails(request,pk):
    drinks = Drinks.objects.get(id=pk)
    serializer = DrinkSerializer(drinks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createDrink(request):
    serializer = DrinkSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def updateDrink(request,pk):
    drink = Drinks.objects.get(id=pk)
    serializer = DrinkSerializer(instance=drink ,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteDrink(request,pk):
    drink = Drinks.objects.get(id=pk)
    drink.delete()


    return Response('Drink Deleted')