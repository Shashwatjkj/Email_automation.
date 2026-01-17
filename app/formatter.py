def format_message(text: str) -> str:
    """
    Keep message exactly as it comes.
    Only clean Telegram markdown and normalize line breaks.
    """

    if not text:
        return ""

    # Remove Telegram markdown stars
    text = text.replace("****", "")
    text = text.replace("**", "")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing spaces from each line (does NOT change spacing structure)
    lines = [line.rstrip() for line in text.split("\n")]

    return "\n".join(lines).strip()
