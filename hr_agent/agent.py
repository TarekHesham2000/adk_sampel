from google.adk.agents import Agent
import csv

def read_csv():
    """
    Reads a CSV file and returns the content as a list of rows (dicts).

    Args:
        filename (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries representing the CSV rows.
    """
    filename = "hr_agent/fake_arabic_candidates.csv"

   
    with open(filename, 'r') as file:
        return list(csv.reader(file))



# Define the root agent for your application
root_agent = Agent(
    # A unique name for your agent [cite: 167, 639]
    name="my_hr_agent",

    # Specify the Gemini model to use (ensure compatibility with AI Studio key) [cite: 19, 56, 168, 645]
    model="gemini-2.0-flash-exp", # Or "gemini-1.0-pro" etc.

    # A brief description of what the agent does [cite: 169, 642]
    description="A basic agent that can chat.",

    # Instructions guiding the agent's behavior and persona [cite: 171, 648]
    instruction="help with HR related tasks and read csv candidates file and create job offer letter",
    # Initially, we won't add specific tools [cite: 172, 659]
    tools=[read_csv]
)

print(f"Agent '{root_agent.name}' defined.")