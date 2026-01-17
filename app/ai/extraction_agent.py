import os
from typing import List, Dict
from dotenv import load_dotenv


from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------
load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    raise RuntimeError("GEMINI_API_KEY not set")


# --------------------------------------------------
# LLM (deterministic)
# --------------------------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


# --------------------------------------------------
# EXTRACTION PROMPT (VERY IMPORTANT)
# --------------------------------------------------


prompt = ChatPromptTemplate.from_template("""
You are a STRICT job information extraction agent.

Your task:
From the given message, extract ONLY essential job-related information.
Ignore emojis, referral alerts, decorative text, and unrelated content.

---------------- SELECTION RULES ----------------

SELECT a job ONLY IF:
1. It contains at least ONE email address
2. The role is TECHNICAL, such as:
   - Software / Developer / Engineer
   - Full Stack / Backend / Frontend / Web
   - AI / ML / Data / Cloud / DevOps
   - Android / iOS / Java / Python / Node / React

REJECT roles such as:
- UI / UX / Designer
- Product Manager / Product Management
- Business Analyst
- HR / Recruiter / Marketing / Sales

---------------- EXTRACTION RULES ----------------

From each valid job, extract ONLY the following fields:

- company: company name (if present)
- role: technical job title

- summary:
  A short, clean paragraph (3–5 lines) describing:
  - what the job is about
  - core responsibilities
  - expectations from the candidate
  - non-technical requirements (learning mindset, collaboration, etc.)
  Do NOT include emojis, alerts, or apply instructions.

- requirements:
  Responsibilities / eligibility / requirements as a LIST

- languages:
  Programming languages only (e.g. Java, Python, JavaScript)

- tech_stack:
  Frameworks, libraries, platforms (e.g. React, Spring Boot, AWS)

- tools:
  Tools or systems (e.g. Git, Docker, Kubernetes)

- emails:
  All email addresses mentioned

IMPORTANT:
- Do NOT include emojis
- Do NOT include referral alerts or headers
- Do NOT include apply links
- Do NOT add explanations
- Do NOT add marketing language
- Extract facts only

---------------- OUTPUT FORMAT ----------------

Return STRICT JSON ONLY.

If no valid technical job exists:
[]

If valid jobs exist:
[
  {{
    "company": "<company name>",
    "role": "<technical role>",
    "summary": "<clean human-readable summary without emojis>",
    "requirements": ["requirement 1", "requirement 2"],
    "languages": ["Java", "Python"],
    "tech_stack": ["Spring Boot", "React", "AWS"],
    "tools": ["Git", "Docker"],
    "emails": ["email@example.com"]
  }}
]

---------------- MESSAGE ----------------
{message}
""")




# --------------------------------------------------
# Parser (enforces JSON)
# --------------------------------------------------
parser = JsonOutputParser()


# --------------------------------------------------
# Chain
# --------------------------------------------------
chain = prompt | llm | parser


# --------------------------------------------------
# Public function
# --------------------------------------------------
def extract_technical_jobs(message: str) -> List[Dict]:
    """
    Returns a list of valid technical job postings with email.
    Returns [] if none found.
    """
    if not message or not message.strip():
        return []

    try:
        result = chain.invoke({"message": message})

        # Safety check
        if isinstance(result, list):
            return result

        return []

    except Exception as e:
        print("Extraction Agent Error:", e)
        return []
