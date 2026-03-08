import json
from google import genai
import todo_service

client = genai.Client(api_key="YOUR_API_KEY")


def agent(query: str):

    prompt = f"""
You are a task manager assistant.

User request:
{query}

Decide if the user wants to:
- add_task
- get_tasks
- update_task
- delete_task

Return JSON with:
function_name
arguments
"""

    response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=prompt
)

    text = response.text

    try:
        data = json.loads(text)
    except:
        return text

    function_name = data.get("function_name")
    arguments = data.get("arguments", {})

    if function_name == "add_task":
        result = todo_service.add_task(**arguments)

    elif function_name == "get_tasks":
        result = todo_service.get_tasks(**arguments)

    elif function_name == "update_task":
        task_id = arguments.pop("task_id")
        result = todo_service.update_task(task_id, **arguments)

    elif function_name == "delete_task":
        result = todo_service.delete_task(**arguments)

    else:
        return "I didn't understand the request."

    return str(result)


# בדיקה מהירה
if __name__ == "__main__":
    while True:
        user_input = input("מה תרצי לעשות? ")
        print(agent(user_input))
