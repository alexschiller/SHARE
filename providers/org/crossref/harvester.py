from furl import furl

from share import Harvester


class CrossRefHarvester(Harvester):
    url = 'https://api.crossref.org/v1/works'

    def do_harvest(self, start_date, end_date):
        start_date = start_date.date()
        end_date = end_date.date()

        return self.fetch_records(furl(self.url).set(query_params={
            'filter': 'from-update-date:{},until-update-date:{}'.format(
                start_date.isoformat(),
                end_date.isoformat()
            ),
            'rows': 1000
        }).url)

    def fetch_records(self, url):
        resp = self.requests.get(url)
        resp.raise_for_status()
        total = resp.json()['message']['total-results']
        records = resp.json()['message']['items']

        # return the first 1000 records
        for record in records:
            yield (record['DOI'], record)

        # make requests for the remaining records
        for i in range(1000, total, 1000):
            response = self.requests.get(furl(url).add(query_params={
                'offset': i
            }).url)

            response.raise_for_status()
            records = response.json()['message']['items']
            for record in records:
                yield (record['DOI'], record)
