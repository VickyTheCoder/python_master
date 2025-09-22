from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EnquirySerializer


class EnquiryAPIView(APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Success return is working!")  
            return Response({"success": True, "data": serializer.data}, status=status.HTTP_201_CREATED)
        print("Error return is working!")  
        return Response({"success": False, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)