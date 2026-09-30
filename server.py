# server.py
# Main server for the SkinSense website
# Uses only Python built-in modules

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import pages


class SkinSenseServer(BaseHTTPRequestHandler):

    def do_GET(self):
        routes = {
            "/": pages.home_page,
            "/product": pages.product_page,
            "/how-it-works": pages.how_it_works_page,
            "/science": pages.science_page,
            "/insights": pages.insights_page,
            "/about": pages.about_page,
            "/contact": pages.contact_page,
            "/waitlist": pages.waitlist_page,
        }

        if self.path == "/logo.png":
            try:
                with open("logo.png", "rb") as image:
                    self.send_response(200)
                    self.send_header("Content-type", "image/png")
                    self.end_headers()
                    self.wfile.write(image.read())
                return
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                return

        try:
            page_function = routes.get(self.path, pages.home_page)
            html_content = page_function()
            self.send_response(200)
        except Exception as error:
            html_content = "<h1>Error</h1><p>" + str(error) + "</p>"
            self.send_response(500)

        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))

    def do_POST(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length).decode("utf-8")
            form = parse_qs(post_data)

            name = form.get("name", [""])[0]
            email = form.get("email", [""])[0]

            if self.path == "/submit":
                message = form.get("message", [""])[0]
                with open("data.txt", "a") as file:
                    file.write("CONTACT | Name: " + name + " | Email: " + email + " | Message: " + message + "\n")
                heading = "Thank You!"
                body = "We received your message, " + name + ". We will reply to " + email + " soon."

            elif self.path == "/submit-waitlist":
                skintype = form.get("skintype", [""])[0]
                with open("waitlist.txt", "a") as file:
                    file.write("WAITLIST | Name: " + name + " | Email: " + email + " | Skin: " + skintype + "\n")
                heading = "You are on the List!"
                body = "Thanks, " + name + ". We will notify you at " + email + " when DermaSense launches."

            else:
                heading = "Unknown Form"
                body = "Something went wrong."

            response = """<html><body style="font-family:Arial; text-align:center; padding:5rem;">
            <h1 style="color:#3b7ea1;">""" + heading + """</h1>
            <p>""" + body + """</p>
            <a href="/" style="color:#3b7ea1;">Back to Home</a>
            </body></html>"""

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(response.encode("utf-8"))

        except Exception as error:
            print("Error:", error)
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Something went wrong.")


def run_server():
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), SkinSenseServer)
    print("SkinSense website running at http://" + host + ":" + str(port))
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()


if __name__ == "__main__":
    run_server()