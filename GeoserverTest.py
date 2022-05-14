import timeit

import requests


def wmts_request(zoom=1):
    for row in range(2 ** zoom):
        for col in range(2 ** (zoom + 1)):
            requests.get(
                f'http://localhost:8080/geoserver/gwc/service/wmts?service=WMTS&version=1.0.0&request=GetTile'
                f'&tilematrixset=EPSG:4326&tilematrix=EPSG:4326:{zoom}&layer=test%3ANatural%20Earth%201&tilerow='
                f'{row}&tilecol={col}&format=image/png')


for i in range(5):
    print(f'{i} level')
    print(timeit.timeit(lambda: requests.get(
        f'http://localhost:8080/geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=test%3ANatural%20Earth'
        f'%201&bbox=-180.0%2C-90.0%2C180.0%2C90.0&width={256 * 2 ** (i + 1)}&height='
        f'{256 * 2 ** i}&srs=EPSG%3A4326&styles=&format=image/png'),
                        number=3) / 3)

    print(timeit.timeit(f'wmts_request({i})', setup="from __main__ import wmts_request", number=3) / 3)
