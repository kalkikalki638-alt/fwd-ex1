from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
</head>
<body>
    <h1>TCP/IP Protocol Suite</h1>
    <h2>Available Protocols</h2>

    <h3>1. Application Layer</h3>
    <ul>
        <li>HTTP - Hypertext Transfer Protocol</li>
        <li>HTTPS - Hypertext Transfer Protocol Secure</li>
        <li>FTP - File Transfer Protocol</li>
        <li>SMTP - Simple Mail Transfer Protocol</li>
        <li>DNS - Domain Name System</li>
        <li>DHCP - Dynamic Host Configuration Protocol</li>
        <li>Telnet - Terminal Network</li>
    </ul>

    <h3>2. Transport Layer</h3>
    <ul>
        <li>TCP - Transmission Control Protocol</li>
        <li>UDP - User Datagram Protocol</li>
    </ul>

    <h3>3. Internet Layer</h3>
    <ul>
        <li>IP - Internet Protocol</li>
        <li>ICMP - Internet Control Message Protocol</li>
        <li>IGMP - Internet Group Management Protocol</li>
        <li>ARP - Address Resolution Protocol</li>
    </ul>

    <h3>4. Network Access Layer</h3>
    <ul>
        <li>Ethernet</li>
        <li>Wi-Fi</li>
        <li>PPP - Point-to-Point Protocol</li>
    </ul>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()



