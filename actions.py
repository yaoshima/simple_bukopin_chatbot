from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet

import pyodbc
import locale

locale.setlocale( locale.LC_ALL, 'id' )

class ResetBalanceFormSlot(Action):

    def name(self):
        return "reset_balance_form_slot"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("account_number", None)]

class AccountBalanceForm(FormAction):
    def name(self) -> Text:
        return "account_balance_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["account_number"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.2.62.231;DATABASE=DATA201812;UID=sa;PWD=Bukopin@)!%')
        cursor = cnxn.cursor()

        acno = int(tracker.get_slot('account_number')) 
        cursor.execute("SELECT NAMA, BLCUR from DWHSA where ACNO = ?", acno)
        row = cursor.fetchone()

        if row:
            account_balance = locale.currency( row.BLCUR, grouping=True )
            name = row.NAMA.strip()
            
            dispatcher.utter_message(f'Yth. {name}, Saldo Anda Saat Ini Adalah {account_balance}')
            print(account_balance)            
        else:
            dispatcher.utter_message("Data Yang Diinput Tidak Sesuai")

        return []



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
