from lib.chat_listener import setup_chat_event_handlers
from lib.log_listener import setup_log_event_handlers
from lib.email_listener import setup_email_event_handlers

from lib.user import register_new_user, password_forgotten
from lib.plan import upgrade_plan

# initialize the event structure
setup_chat_event_handlers()
setup_log_event_handlers()
setup_email_event_handlers()


# register a new user
register_new_user("ssss", "ss", "hi@sssss.com")

# send a password reset message
password_forgotten("hi@sssss.com")

# upgrade the plan
upgrade_plan("hi@sssss.com")