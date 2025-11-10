import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown_museo(self):
        try:
            musei = self._model.get_musei()
            if not musei:
                self._view.show_alert('Museo non trovato')
                return
            opzioni = [ft.dropdown.Option("Nessun filtro",  "NESSUN_FILTRO")]
            for m in musei:
                opzioni.append(ft.dropdown.Option(m.nome))
            self._view.dd_museo.options = opzioni
            self._view.update()
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento dei musei: {e}")

    def popola_dropdown_epoca(self):
        try:
            epoche = self._model.get_epoche()
            if not epoche:
                self._view.show_alert('Nessuna epoca trovata')
                return
            opzioni = [ft.dropdown.Option("Nessun filtro",  "NESSUN_FILTRO")]
            for e in epoche:
                opzioni.append(ft.dropdown.Option(e))
            self._view.dd_epoca.options = opzioni
            self._view.update()
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento delle epoche: {e}")

    # CALLBACKS DROPDOWN
    # TODO
    def handler_dropdown_museo(self,e):
        if e.control.value == "NESSUN_FILTRO":
            self.museo_selezionato = None
        else:
            self.museo_selezionato = e.control.value

    def handler_dropdown_epoca(self,e):
        if e.control.value == "NESSUN_FILTRO":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = e.control.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self,e):
        try:
            artefatti = self._model.get_artefatti_filtrati(museo=self.museo_selezionato,epoca=self.epoca_selezionata)
            musei = self._model.get_musei()
            museo_id_nome = {}
            for m in musei:
                museo_id_nome[m.id] = m.nome

            self._view.txt_lista_artefatti.controls.clear()
            if not artefatti:
                self._view.show_alert('Nessun artefatto trovato per i filtri selezionati')
                self._view.update()
                return

            for a in artefatti:
                museo_nome = museo_id_nome.get(a.id_museo, "Museo non trovato")
                self._view.txt_lista_artefatti.controls.append(ft.Text(f"{a.nome}, {a.epoca}, {a.tipologia}, Museo: {museo_nome}"))
            self._view.update()
        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento degli artefatti: {e}")
