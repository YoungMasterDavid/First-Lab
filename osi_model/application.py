import json

# Application Layer (Handles user requests, HTTP-like)
class ApplicationLayer:
    def send_data(self, message):
        print("[Application Layer] Creating request")
        request = json.dumps({"method": "GET", "data": message})
        return request

    def receive_data(self, request):
        print("[Application Layer] Processing response")
        response = json.loads(request)
        return response["data"]