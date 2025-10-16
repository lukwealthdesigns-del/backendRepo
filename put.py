from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Mock database
data = [
    {
        "id": 1,
        "name": "Lukman Ibrahim",
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    # ---------- PUT (Update existing data) ----------
    def do_PUT(self):
        # Read the request body length
        content_length = int(self.headers['Content-Length'])
        # Read the actual request body
        body = self.rfile.read(content_length)
        # Convert JSON text to Python dictionary
        update_data = json.loads(body)

        # Look for the record to update
        for item in data:
            if item["id"] == update_data["id"]:
                item.update(update_data)
                self.send_data({"message": "Data updated", "data": item})
                return

        # If not found
        self.send_data({"error": "Item not found"}, 404)


def run():
    print("PUT API is running on http://localhost:8000")
    server = HTTPServer(('localhost', 8000), BasicAPI)
    server.serve_forever()

run()
