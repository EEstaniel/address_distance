# Address Distance

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)

A Django microservice that calculates the distance between two addresses.

# Installation

1. Recommended to use a virtual environment
2. pip install -r requirements.txt

5. Start using `python manage.py runserver`

# Usage

Default use:
    
    [POST REQUEST]
    
    http://localhost:/api/distance/

Input data:

    JSON DATA:
    {
        origin: [street][city][state][zip/postal code]
        destination: [address2]
    }

    EXAMPLE:

    {
        origin: 1500 NW Bethany Blvd, Beaverton, Oregon, 97006
        destination: 5250 Campanile Dr, San Diego, CA, 92182
    }

Output data:
    
    {
        "destination_addresses" : [ "2901 W Ball Rd, Anaheim, CA 92804, USA" ],
        "origin_addresses" : [ "7655 Hollywood Blvd, Los Angeles, CA 90046, USA" ],
        "rows" : [
            {
                "elements" : [
                    {
                        "distance" : {
                            "text" : "54.1 km",
                            "value" : 54097
               },
                        "duration" : {
                            "text" : "51 mins",
                            "value" : 3081
               }, 
                        "status" : "OK" }]}],
                "status" : "OK"
    }