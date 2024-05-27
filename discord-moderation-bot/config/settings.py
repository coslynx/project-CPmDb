# settings.py (Python)

import os
from dotenv import load_dotenv

load_dotenv()

# Discord Bot Token
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Customizable Word Filters
WORD_FILTERS = ["badword1", "badword2", "badword3"]

# User Activity Tracking
ACTIVITY_THRESHOLD = 5

# Automated Warning and Mute System
WARNING_THRESHOLD = 3
MUTE_DURATION = 600  # 10 minutes in seconds

# Role Management
MODERATOR_ROLE = "Moderator"
MUTED_ROLE = "Muted"

# Scheduled Tasks
CLEANUP_INTERVAL = 3600  # 1 hour in seconds

# Customizable Commands
COMMAND_PREFIX = "!"

# Monitoring
MONITORING_CHANNEL = "moderation-logs"

# Updates and Improvements
UPDATE_INTERVAL = 86400  # 1 day in seconds