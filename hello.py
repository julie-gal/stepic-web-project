import re

def app(environ, start_response):
    qs = environ['QUERY_STRING']
    pattern = r"[0-9A-Za-z]+=[0-9A-za-z]+|[0-9A-Za-z]+="
    result = []
    if re.search(pattern, qs):
        result = re.findall(pattern, qs)
    result = "\r\n".join(result)
    start_response("200 OK", [
        ("Content-Type", "text/plain")])
    return [i.encode() for i in result]
   
    
