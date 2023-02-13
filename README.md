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
        "destination_addresses": [
            "SW Campus Way, Corvallis, OR 97331, USA"
        ],
        "origin_addresses": [
            "300 NW 3rd St, Corvallis, OR 97330, USA"
        ],
        "rows": [
            {
                "elements": [
                    {
                        "distance": {
                            "text": "2.4 km",
                            "value": 2401
                        },
                        "duration": {
                            "text": "7 mins",
                            "value": 432
                        },
                        "status": "OK",
                        "distance_mi": {
                            "text": "3.86 mi"
                        }
                    }
                ]
            }
        ],
        "status": "OK"
    }