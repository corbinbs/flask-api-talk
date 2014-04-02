from hubology.views import FlaskAPI


class PyTruck(FlaskAPI):
    def index(self):
        """
            Get a list of information about the fleet of PyTrucks
        """
        return [
            {
                'id': 1,
                'make': 'Ford',
                'model': 'F-350',
                'year': '2004',
                'lab': {
                    'workstations': 6,
                    'solar_powered': True
                }
            },
            {
                'id': 2,
                'make': 'Ford',
                'model': 'F-250',
                'year': '1999',
                'lab': {
                    'workstations': 4,
                    'solar_powered': False
                }
            },
            {
                'id': 3,
                'make': 'Ford',
                'model': 'F-550',
                'year': '2012',
                'lab': {
                    'workstations': 8,
                    'solar_powered': True
                }
            },
        ]

    def get(self, id):
        """
            Get status information about a specific PyTruck
        """
        #Just uses mock data for demo
        return {
            'id': id,
            'make': 'Ford',
            'model': 'F-350',
            'year': '2004',
            'lab': {
                'workstations': 6,
                'solar_powered': True
            }
        }

    def post(self):
        """
            Create a new PyTruck and put it into service
        """
        pass

    def put(self, id):
        """
            Update information about an existing PyTruck
        """
        pass