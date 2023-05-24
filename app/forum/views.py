import aiohttp_jinja2
from aiohttp import wev


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'title': 'Some test text'}
