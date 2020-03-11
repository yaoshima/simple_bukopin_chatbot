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

