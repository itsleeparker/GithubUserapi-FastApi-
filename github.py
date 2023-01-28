import requests

class apiConfig:
    Accept:str
    def __init__(self) -> None:
        self.Accept = "application/vnd.github+json";
        pass
    def getConfig(self , beraer):
            return {
                "Accept" : self.Accept , 
                "Authorization" : f'Bearer {beraer}',
            }

class GithubApi:
    baseroute:str = "/github"
    _apiUrl:str
    _config:apiConfig
    _token:str
    def __init__(self) -> None:
        self.Init()
        
    def Init(self)->None:
        self._apiUrl = "https://api.github.com/users"
        self._config = apiConfig()
        self._token = "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"
        
    def List_Users(self):
        try:
            response:any  =  requests.get(self._apiUrl , headers=self._config.getConfig(self._token))
        except :
            raise Exception(f'An Erro Occured')

        return response.json()