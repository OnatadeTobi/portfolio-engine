import cloudinary.uploader
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def upload_image(request):
    file = request.FILES.get('file')
    if not file:
        return Response({"error": "No file provided"}, status=400)

    result = cloudinary.uploader.upload(file, folder="resume_images/")
    return Response({"url": result['secure_url'], "public_id": result['public_id']}, status=201)


@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
def delete_image(request):
    public_id = request.data.get('public_id')
    if not public_id:
        return Response({"error": "No public_id provided"}, status=400)

    cloudinary.uploader.destroy(public_id)
    return Response(status=204)
