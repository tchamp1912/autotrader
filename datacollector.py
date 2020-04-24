from alpha_vantage.timeseries import TimeSeries
import tdameritrade as td

from constants import API_KEY
from constants import CLIENT_ID
from constants import ACCOUNT_ID
from constants import REFRESH_TOKEN


class CurrentCollector:

    client: td.TDClient

    def __init__(self):

        self._auth()

        self.client

    def _auth():



class HistoricCollector:

    ts: TimeSeries

    def __init__(self):

        # alpha vantage api wrapper
        self.ts = TimeSeries(key=API_KEY,
                             output_format='pandas',
                             indexing_type='integer',
                             )
