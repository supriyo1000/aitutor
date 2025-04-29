# from rest_framework.views import APIView
# from rest_framework.response import Response
# import openai  # or use deepseek, etc.
# import os
# from dotenv import load_dotenv

# openai.api_key = "your_api_key"

# load_dotenv()

# class AIAgentView(APIView):
#     def post(self, request):
#         user_message = request.data.get("user_message")

#         # Call AI (OpenAI, DeepSeek, etc.)
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an English tutor."},
#                 {"role": "user", "content": user_message}
#             ]
#         )
#         ai_reply = response['choices'][0]['message']['content']
#         return Response({"reply": ai_reply})




from rest_framework.views import APIView
from rest_framework.response import Response
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

class AIAgentView(APIView):
    def post(self, request):
        user_message = request.data.get("user_message")

        # Generate a response using Gemini
        try:
            response = model.generate_content(user_message)
            ai_reply = response.text
        except Exception as e:
            ai_reply = f"Error: {str(e)}"

        return Response({"reply": ai_reply})
