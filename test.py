# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()
# print(os.getenv("OPENAI_API_KEY")[:20])

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )

# try:
#     response = client.responses.create(
#         model="gpt-4.1-mini",
#         input="Hello"
#     )

#     print("SUCCESS")
#     print(response.output_text)

# except Exception as e:
#     print("ERROR:")
#     print(e)

from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

print("Length:", len(key))
print("Starts with:", key[:7])