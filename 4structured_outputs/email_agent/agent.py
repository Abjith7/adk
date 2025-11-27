from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field 

class Emailcontent(BaseModel):
    subject: str= Field(
        description="The subject of the email. should be short and sharp"
    )
    body:str=Field(
        description="The main content of the mail. Should be well structured and customised to the recipient as theuser instructs"
    )
root_agent=LlmAgent(
    name="email_agent",
      model="gemini-2.0-flash",
      instruction="""
        You are an Email Generation Assistant.
        Your task is to generate a professional email based on the user's request.

        GUIDELINES:
        - Create an appropriate subject line (concise and relevant)
        - Write a well-structured email body with:
            * Professional greeting
            * Clear and concise main content
            * Appropriate closing
            * Your name as signature
        - Suggest relevant attachments if applicable (empty list if none needed)
        - Email tone should match the purpose (formal for business, friendly for colleagues)
        - Keep emails concise but complete

        IMPORTANT: Your response MUST be valid JSON matching this structure:
        {
            "subject": "Subject line here",
            "body": "Email body here with proper paragraphs and formatting",
        }

        DO NOT include any explanations or additional text outside the JSON response.
        and the email should be ready to be sent as it is.
        and i dont want any escaped  \n characters in the body part of the response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=Emailcontent,
    output_key="email",
)
# Optional: clean up escaped newlines in the response automatically
def post_process(output):
    try:
        if "email" in output and "body" in output["email"]:
            output["email"]["body"] = output["email"]["body"].encode().decode("unicode_escape")
    except Exception:
        pass
    return output


root_agent.post_process = post_process