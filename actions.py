from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class list_saving_account(Action):
    def name(self) -> Text:
        return "list_saving_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        buttons = [
            {"title": "Tabungan SiAga Bukopin", "payload": "/inform{\"saving_account_type\": \"Tabungan SiAga Bukopin\"}"},
            {"title": "Tabunganku", "payload": "/inform{\"saving_account_type\": \"Tabunganku\"}"},
            {"title": "Wokee", "payload": "/inform{\"saving_account_type\": \"Wokee\"}"}

        ]

        dispatcher.utter_button_message("Berikut jenis tabungan yang tersedia:", buttons)
        return []

class desc_saving_account_type(Action):
    def name(self) -> Text:
        return "desc_saving_account_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        saving_account_type = tracker.get_slot("saving_account_type")

    

        if saving_account_type == "Wokee":
            info = "Tabungan Wokee, Produk Tabungan khusus perorangan yang berbasis elektronik Bank Bukopin"
        elif saving_account_type == "Tabunganku":
            info = "Tabungan perorangan dengan persyaratan mudah dan ringan"
        elif saving_account_type == "Tabungan SiAga Bukopin":
            info = "Tabungan SiAga Bukopin, Simpanan yang penarikannya hanya dapat dilakukan menurut syarat-syarat tertentu"
        else:
            info = ""

        if info != "":
            dispatcher.utter_message(info)
        else:
            dispatcher.utter_message("Tabungan tidak dikenal")

        return []
