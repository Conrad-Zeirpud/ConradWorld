from django.shortcuts import render
from django.http import HttpResponse
from kanban.models import Card
from kanban.models import Column
from rest_framework import generics
from kanban.serializers import ColumnSerializer






class ColumnListAPIView(generics.ListAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer



def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')
