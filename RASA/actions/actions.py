from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        return []

class ActionGoodbye(Action):
    def name(self) -> Text:
        return "action_goodbye"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_goodbye")
        return []

class ActionAffirm(Action):
    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_affirm")
        return []

class ActionDeny(Action):
    def name(self) -> Text:
        return "action_deny"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_deny")
        return []

class ActionAdmissionsInquiry(Action):
    def name(self) -> Text:
        return "action_admissions_inquiry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_admissions_inquiry")
        return []

class ActionAdmissionsInquiryProgram(Action):
    def name(self) -> Text:
        return "action_admissions_inquiry_program"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_admissions_inquiry_program")
        return []

class ActionPlacementsInquiry(Action):
    def name(self) -> Text:
        return "action_placements_inquiry"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_placements_inquiry")
        return []

class ActionApplicationProcess(Action):
    def name(self) -> Text:
        return "action_application_process"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_application_process")
        return []

class ActionFinancialAid(Action):
    def name(self) -> Text:
        return "action_financial_aid"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_financial_aid")
        return []

class ActionAcademicPrograms(Action):
    def name(self) -> Text:
        return "action_academic_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_academic_programs")
        return []

class ActionCampusFacilities(Action):
    def name(self) -> Text:
        return "action_campus_facilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_campus_facilities")
        return []

class ActionRedirectApplication(Action):
    def name(self) -> Text:
        return "action_redirect_application"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_redirect_application")
        return []

class ActionRedirectFacilities(Action):
    def name(self) -> Text:
        return "action_redirect_facilities"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_redirect_facilities")
        return []

class ActionRedirectAdmissions(Action):
    def name(self) -> Text:
        return "action_redirect_admissions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_redirect_admissions")
        return []

class ActionRedirectPrograms(Action):
    def name(self) -> Text:
        return "action_redirect_programs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_redirect_programs")
        return []

class ActionDefault(Action):
    def name(self) -> Text:
        return "action_default"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_default")
        return []
