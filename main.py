from aiohttp import ClientSession, web


async def persistent_session(app):
    app["session"] = session = ClientSession()
    yield
    await session.close()


async def create_app(**__):
    app = web.Application()
    app.router.add_route("GET", r"", hello)
    app.cleanup_ctx.append(persistent_session)
    return app


async def hello(request):
    return web.json_response({"status": "OK"})
