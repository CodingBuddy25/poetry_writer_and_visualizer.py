from dotenv import load_dotenv
from Crew import PoetryCrew

load_dotenv()
try:
    PoetryCrew().crew().kickoff()
except Exception as e:
    raise Exception(f"An error occurred while running the crew: {e}")

