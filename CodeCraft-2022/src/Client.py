class Client:
    """客户节点类"""

    def __init__(self, client_name) -> None:
        self.demand = 0
        self.client_name = client_name