from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass
    #TODO
    @staticmethod
    def leggi_musei():
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor()
            query = "SELECT * FROM museo"
            cursor.execute(query)
            musei = []
            for row in cursor:
                uTemp = Museo(row[0],row[1],row[2])
                musei.append(uTemp)
            cursor.close()
            cnx.close()
            return musei
        except Exception as e:
            print(f"Errore nella lettura dei musei: {e}")
            return None

