## ask_account_balance
* greet
  - utter_greet
  - list_saving_account
* ask_account_balance
  - reset_balance_form_slot
  - account_balance_form
  - form{"name": "account_balance_form"}
  - form{"name": null}
  - utter_greet


## ask_account_balance_direct_repeat
* ask_account_balance
  - account_balance_form
  - form{"name": "account_balance_form"}
  - form{"name": null}
  - utter_greet
* ask_account_balance
  - reset_balance_form_slot
  - account_balance_form
  - form{"name": "account_balance_form"}
  - form{"name": null}
  - utter_greet
* thanks
  - utter_welcome

## ask_account_balance_direct
* ask_account_balance
  - reset_balance_form_slot
  - account_balance_form
  - form{"name": "account_balance_form"}
  - form{"name": null}
  - utter_greet
* thanks
  - utter_welcome


## ask_saving_account_type
* greet
  - utter_greet
  - list_saving_account
* inform{"saving_account_type": "Wokee"}
  - desc_saving_account_type
* thanks
  - utter_welcome

## ask_saving_account_type_no_greeting
* saving_account_info
  - list_saving_account
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
  - desc_saving_account_type
* thanks
  - utter_welcome

## ask_saving_account_multiple_times
* saving_account_info
  - list_saving_account
* inform{"saving_account_type": "Wokee"}
  - desc_saving_account_type
* inform{"saving_account_type": "Tabunganku"}
  - desc_saving_account_type
* thanks
  - utter_welcome

## story_goodbye
* goodbye
  - utter_goodbye

## story_thankyou
* thanks
  - utter_welcome


## interactive_story_1
* greet
    - utter_greet
    - list_saving_account
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
    - slot{"saving_account_type": "Tabungan SiAga Bukopin"}
    - desc_saving_account_type
* saving_account_info
    - list_saving_account
* inform{"saving_account_type": "Tabunganku"}
    - slot{"saving_account_type": "Tabunganku"}
    - desc_saving_account_type
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* inform{"saving_account_type": "Tabunganku"}
    - slot{"saving_account_type": "Tabunganku"}
    - desc_saving_account_type
* saving_account_info
    - list_saving_account
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
    - slot{"saving_account_type": "Tabungan SiAga Bukopin"}
    - desc_saving_account_type
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* affirm
    - list_saving_account
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
    - slot{"saving_account_type": "Tabungan SiAga Bukopin"}
    - desc_saving_account_type
* affirm
    - list_saving_account
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
    - slot{"saving_account_type": "Tabungan SiAga Bukopin"}
    - desc_saving_account_type
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye



## interactive_story_1
* greet
    - utter_greet
    - list_saving_account
* inform{"saving_account_type": "Tabunganku"}
    - slot{"saving_account_type": "Tabunganku"}
    - desc_saving_account_type
* out_of_scope
    - utter_capacity
* affirm
    - list_saving_account
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - list_saving_account
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* affirm
    - list_saving_account
* out_of_scope
    - utter_capacity
* affirm
    - list_saving_account
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
    - list_saving_account
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* greet
    - utter_greet
    - list_saving_account
* inform{"saving_account_type": "Tabunganku"}
    - slot{"saving_account_type": "Tabunganku"}
    - desc_saving_account_type
* affirm
    - list_saving_account
* thanks
    - utter_welcome
* goodbye
    - utter_goodbye

## interactive_story_1
* saving_account_info
    - list_saving_account
* inform{"saving_account_type": "Tabungan SiAga Bukopin"}
    - slot{"saving_account_type": "Tabungan SiAga Bukopin"}
    - desc_saving_account_type
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* affirm
    - list_saving_account
* greet
    - utter_greet
    - list_saving_account
* thanks
    - utter_welcome

## interactive_story_1
* greet
    - utter_greet
    - list_saving_account
* goodbye
    - utter_goodbye
* out_of_scope
    - utter_capacity
* saving_account_info
    - list_saving_account
* inform{"saving_account_type": "Wokee"}
    - slot{"saving_account_type": "Wokee"}
    - desc_saving_account_type
* goodbye
    - utter_goodbye

