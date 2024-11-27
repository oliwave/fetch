class Endpoint:

    """Endpoint is the target API for health check"""
    
    def __init__(self, name: str, url: str, method="GET", headers=None, body=None):
        self.__name = name
        self.__url = url
        self.__domain = url.split("//")[-1].split("/")[0]
        self.__method = method
        self.__headers = headers or {}
        self.__body = body

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self.__name = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        if not value.startswith("http"):
            raise ValueError("Invalid URL")
        self.__url = value

    @property
    def domain(self):
        return self.__domain

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        valid_methods = {"GET", "POST", "PUT", "DELETE", "PATCH"}
        if value[0] not in valid_methods:
            raise ValueError(f"{value[0]} Method must be one of {valid_methods}")
        self.__method = value[0]

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, value):
        value = value[0]
        if not isinstance(value, dict):
            value = {}
        self.__headers = value

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        if value[0] is not None and not isinstance(value[0], (str, dict)):
            raise ValueError("Body must be a string, dictionary, or None")
        self.__body = value[0]

    def __repr__(self):
        return (
            f"Endpoint(name={self.name}, url={self.url}, method={self.method}, "
            f"headers={self.headers}, body={self.body})"
        )
