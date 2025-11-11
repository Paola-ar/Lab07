from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()
        self.artefatti_filtrati = []
        self.epoche = []
        self.musei = []

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        artefatti = self._artefatto_dao.leggi_artefatti()
        artefatti_filtrati = []
        musei = self.get_musei()
        museo_id_nome = {}
        for m in musei:
            museo_id_nome[m.id] = m.nome
        for a in artefatti:
            museo_nome = museo_id_nome.get(a.id_museo,None)

            if museo is not None and museo_nome != museo:
                continue

            if epoca is not None and a.epoca != epoca:
                continue

            artefatti_filtrati.append(a)
        #self.artefatti_filtrati = artefatti_filtrati
        return artefatti_filtrati


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        self.epoche = self._artefatto_dao.leggi_epoche()
        return self.epoche


    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        self.musei = self._museo_dao.leggi_musei()
        return self.musei


