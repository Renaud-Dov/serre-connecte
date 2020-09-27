

from miflora.miflora_poller import MiFloraPoller
from btlewrap.bluepy import BluepyBackend
import time
class Capteur(MiFloraPoller):
    def __init__(self, mac,backend=BluepyBackend):
        super().__init__(mac, backend)
    def valeurs(self):
        valeur={'humidite:':self.parameter_value('moisture',False),
                'temperature':self.parameter_value('temperature',False),
                'light':self.parameter_value('light',False),
                'conductivity/fertilite':self.parameter_value('conductivity',False),
                }
        return valeur
    def test(self):
        self.fill_cache()
        if self.cache_available() and (len(self._cache) == 16):
            print(len(self._cache),self.cache_available())
            return self.parse_data()
    def batterie(self):
        self.battery_level()
    def name(self):
        self.poller.name()
    
captor=Capteur("80:EA:CA:89:5F:EA", BluepyBackend)
# poller = MiFloraPoller("80:EA:CA:89:5F:EA", BluepyBackend)
def times(x):
    for loop in range(x):
        print(x-loop)
        time.sleep(1)
    print()
for i in range (100):

   
# print(captor.valeurs())#,poller.fetch_history())
    # # print(poller.cache_available())

# print()
# print(captor.is_ropot())
    print(time.time(),captor.test())
    times(3)
