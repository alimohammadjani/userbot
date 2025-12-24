Telegram Members Exporter Scripts
This repository contains two Python scripts for exporting members of a Telegram group or channel to a CSV file using the Telethon library.

1. 1.py
Description:

Exports all members of a Telegram group to members.csv.
Reads API credentials and group info from environment variables.
Handles Telegram rate limits automatically.
Uses logging for progress and error reporting.
Environment Variables:

TELEGRAM_API_ID: Your Telegram API ID
TELEGRAM_API_HASH: Your Telegram API Hash
GROUP: The group username (e.g., @mygroup) or group ID
Usage:

export TELEGRAM_API_ID=123456
export TELEGRAM_API_HASH=your_api_hash
export GROUP=@yourgroup
python 1.py
2. 2.py
Description:

Exports all members of a Telegram group or channel to a CSV file (filename can be set via env).
Reads API credentials, session name, group/channel, and output file from environment variables.
Handles Telegram rate limits, admin requirements, and private channels.
Uses logging for progress and error reporting.
Environment Variables:

TELEGRAM_API_ID: Your Telegram API ID
TELEGRAM_API_HASH: Your Telegram API Hash
CHANNEL_OR_GROUP: The group/channel username (e.g., @mygroup) or ID
SESSION_NAME: (Optional) Session file name (default: session_name)
OUTFILE: (Optional) Output CSV file name (default: members.csv)
Usage:

export TELEGRAM_API_ID=123456
export TELEGRAM_API_HASH=your_api_hash
export CHANNEL_OR_GROUP=@yourgroup
# Optional:
# export SESSION_NAME=my_session
# export OUTFILE=output.csv
python 2.py
Notes
The scripts will prompt for login the first time and save a session file.
Do not share your API credentials or session files publicly.
Add session files (e.g., session_name.session) to your .gitignore before uploading to GitHub.
License
MIT