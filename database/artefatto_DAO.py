from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_epoche():
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor()
            cursor.execute('SELECT DISTINCT epoca FROM artefatto ORDER BY epoca')
            epoche = []
            for row in cursor:
                epoche.append(row[0])
            cursor.close()
            cnx.close()
            return epoche
        except Exception as e:
            print(f"Errore nella lettura delle epoche: {e}")
            return None

    def leggi_artefatti(self):
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM artefatto")
            artefatti = []
            for row in cursor:
                uTemp = Artefatto(row[0], row[1], row[2], row[3], row[4])
                artefatti.append(uTemp)
            cursor.close()
            cnx.close()
            return artefatti

        except Exception as e:
            print(f"Errore nella lettura delle epoche: {e}")
            return None
