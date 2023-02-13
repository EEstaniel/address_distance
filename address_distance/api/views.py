import requests
import googlemaps
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .config import key

@api_view(['POST'])
def distance(request):
    # Google API Key for Distance Matrix API

    gmaps = googlemaps.Client(key=key)

    geocode_1 = gmaps.geocode(request.data['origin'])
    geocode_2 = gmaps.geocode(request.data['destination'])

    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins=place_id:{geocode_1[0]['place_id']}&destinations=place_id:{geocode_2[0]['place_id']}&key={key}"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return Response(response.text)

