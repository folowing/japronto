from japronto import Application

def dump(request):
    text = """
Method: {0.method}
Path: {0.path}
Version: {0.version}
Headers: {0.headers}
Match: {0.match_dict}
Body: {0.body}
QS: {0.query_string}
query: {0.query}
mime_type: {0.mime_type}
encoding: {0.encoding}
form: {0.form}
files: {0.files}
keep_alive: {0.keep_alive}
route: {0.route}
hostname: {0.hostname}
port: {0.port}
remote_addr: {0.remote_addr},
cookies: {cookies}
""".strip().format(request, cookies={k: (m.value, m) for k, m in request.cookies.items()})

    return request.Response(text=text)

app = Application()
app.router.add_route('/', dump)
app.router.add_route('/{a}/{b}', dump)

app.run()
