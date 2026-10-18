
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA

load_dotenv()

try:
    model = ChatNVIDIA(
        model="nvidia/nemotron-3-super-120b-a12b",
        temperature=0
    )

    response = model.invoke(
        "Reply with exactly: NVIDIA connection successful"
    )

    print(response.content)

except Exception as error:
    print("Connection test failed:", type(error).__name__)
    print(error)
