

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactSerializer
from .models import ContactMessage



class ContactSubmitView(APIView):
    def post(self, request):
        print("=== POST HIT ===") 
        print(request.data)

        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Optional: send an email notification to you
            send_mail(
                subject=f"New Contact Form Submission from {contact.name}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\n\nMessage:\n{contact.message}",
                from_email=contact.email,
                recipient_list=['austinchiwambo081@gmail.com'],  
                fail_silently=False,
            )

            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
        print("Serializer errors:", serializer.errors) 
        return Response({"received": request.data, "errors": serializer.errors}, status=400)

    
    
