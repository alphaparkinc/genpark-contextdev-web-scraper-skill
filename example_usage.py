from client import ContextDevScraperClient
client = ContextDevScraperClient()
print(client.parse_html("<html><body><p>Hello world</p></body></html>"))