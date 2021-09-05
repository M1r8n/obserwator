from classes.chat import post_chat_message
from .event import subscribe

def handle_user_registered_event(user):
    post_chat_message("sales",
        f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.")

def handle_user_upgrade_plan_event(user):
    post_chat_message("sales",
        f"{user.name} has upgraded their plan.")

def setup_chat_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_upgrade_plan", handle_user_upgrade_plan_event)