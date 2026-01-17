from typing import Union, List


def format_message(text: Union[str, List[str]]) -> str:
    """
    Format Telegram message content.

    - Accepts string OR list of strings
    - Preserves original spacing and line breaks
    - Removes Telegram markdown (** / ****)
    """

    if not text:
        return ""

    # ✅ If message comes as list of strings → join them
    if isinstance(text, list):
        text = "\n\n".join(item for item in text if item)

    # Ensure text is string
    if not isinstance(text, str):
        return ""

    # Remove Telegram markdown stars
    text = text.replace("****", "")
    text = text.replace("**", "")

    # Normalize line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing spaces per line (keep structure)
    lines = [line.rstrip() for line in text.split("\n")]

    return "\n".join(lines).strip()
