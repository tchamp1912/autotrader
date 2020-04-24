import json
import logging
import websocket

from constants import API_KEY, STOCK_SOCKET


class StockStream():

    ws: websocket.WebsocketApp
    subscriptions: list = []
    logger: logging.Logger

    def __init__(self, socket_address: str):

        # intialize logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # open web socket to Polygon
        self.ws = websocket.WebSocketApp(
                                         STOCK_SOCKET,
                                         on_open=self._socket_open,
                                         on_message=self._on_message,
                                         on_close=self._on_close,
                                         )
        # run socket until close
        self.ws.run_forever()

    @classmethod
    def _socket_open(cls):

        # authorize connection
        auth_d = {
            "action": "auth",
            "params": API_KEY
        }

        cls.logger.info("Authorizing API Key")
        # send credentials
        cls.ws.send(json.dumps(auth_d))

    @classmethod
    def _on_message(cls, message: str):

        # log message recieved
        cls.logger.info(message)

    def subscribe(self, ticker: str):

        # add new ticker to subscriptions
        self.subscriptions += f"Q.{ticker}"

        # subcribe to new ticker
        channel_d = {
            "action": "subscription",
            "params": self.subscriptions
        }

        # send updated channel list
        self.ws.send(json.dumps(channel_d))
