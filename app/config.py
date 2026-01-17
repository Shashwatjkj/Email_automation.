import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
GROUP_ID = -1002947896517

if not API_ID or not API_HASH:
    raise RuntimeError("API_ID or API_HASH missing")
