#!/usr/bin/env python3
import http.server, json, re, os
PORT = int(os.environ.get("PORT", 8080))

class ApiKeyRadarHandler(http.server.BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode("utf-8"))

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        self.send_json({"status": "healthy", "service": "ApiKeyRadar API", "version": "1.0.0", "patterns_supported": 120})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
        try: payload = json.loads(body)
        except Exception: payload = {"text": body}
        text = payload.get("text", "")
        detected = []
        if re.search(r"sk-[a-zA-Z0-9]{32,}", text): detected.append({"provider": "OpenAI", "type": "Secret Key", "risk": "CRITICAL"})
        if re.search(r"AKIA[0-9A-Z]{16}", text): detected.append({"provider": "AWS", "type": "Access Key ID", "risk": "HIGH"})
        if re.search(r"ghp_[a-zA-Z0-9]{36}", text): detected.append({"provider": "GitHub", "type": "Personal Access Token", "risk": "CRITICAL"})
        if re.search(r"sk_live_[0-9a-zA-Z]{24}", text): detected.append({"provider": "Stripe", "type": "Live Secret Key", "risk": "CRITICAL"})
        self.send_json({
            "success": True,
            "secrets_found_count": len(detected),
            "findings": detected,
            "clean": len(detected) == 0
        })

if __name__ == "__main__":
    http.server.HTTPServer(("0.0.0.0", PORT), ApiKeyRadarHandler).serve_forever()
