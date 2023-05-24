from aiohttp import web
import jinja2
import aiohttp_jinja2


def setup_routes(application) -> None:
    pass


def setup_external_libraries(
        application: web.Application) -> None:
    aiohttp_jinja2.setup(
        application, loader=jinja2.FileSystemLoader('templates'))


def setup_app(application: web.Application) -> None:
    setup_external_libraries(application)
    setup_routes(application)
    print('app setup succeed')

app = web.Application()


if __name__ == '__main__':
    setup_app(app)
    web.run_app(app)