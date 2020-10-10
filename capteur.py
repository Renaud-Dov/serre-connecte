from miflora.miflora_poller import MiFloraPoller
from btlewrap.bluepy import BluepyBackend
import time
class Capteur(MiFloraPoller):
    def __init__(self, mac,backend=BluepyBackend):
        super().__init__(mac, backend)
    def valeurs(self):
        self.fill_cache()
        if self.cache_available() and (len(self._cache) == 16):
            print(len(self._cache),self.cache_available())
            return self._parse_data()
    def batterie(self):
        self.battery_level()
    def nameCapteur(self):
        self.name()
    
# print(captor.valeurs())#,poller.fetch_history())