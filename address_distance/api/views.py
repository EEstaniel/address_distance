import requests
import googlemaps
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .config import key

@api_view(['POST'])
def distance(request):
    """
    POST request that takes in a request with JSON data: origin and destination.
    This then converts the addresses into a geocode in order to retrieve the place_id to use for the url request.
    This then returns data regarding the addresses and includes the distance between them.

    :param request: {origin: [address1], destination: [address2]}
    :return: Json data
    """

    # initialize googlemaps api key
    gmaps = googlemaps.Client(key=key)

    # convert origin and destination to geocodes to retrieve the location's place_id.
    geocode_1 = gmaps.geocode(request.data['origin'])
    geocode_2 = gmaps.geocode(request.data['destination'])

    # initialize url to use Google's Distance Matrix API
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins=place_id:{geocode_1[0]['place_id']}&destinations=place_id:{geocode_2[0]['place_id']}&key={key}"

    # initialize payload, headers, and response.
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload).json()

    # get distance in km and convert to miles
    addr_distance_km = float(response["rows"][0]['elements'][0]['distance']['text'].split(' ')[0])
    miles = round(addr_distance_km / 1.609, 1)

    # add distance_mi to response
    response["rows"][0]['elements'][0]['distance_mi'] = {'text': f'{miles} mi'}

    # return JSON data
    return Response(response)

