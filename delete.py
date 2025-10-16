from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "id": 1,
        "name": "Lukman Ibrahim",
        "track": "AI Developer"
    },
    {
        "id": 2,
        "name": "Aisha Musa",
        "track": "Backend Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    # ---------- DELETE (Remove data) ----------
    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        delete_data = json.loads(body)

        # Search for the item to delete
        for item in data:
            if item["id"] == delete_data["id"]:
                data.remove(item)
                self.send_data({"message": "Item deleted successfully"})
                return

        self.send_data({"error": "Item not found"}, 404)


def run():
    print("DELETE API is running on http://localhost:8000")
    server = HTTPServer(('localhost', 8000), BasicAPI)
    server.serve_forever()

run()
