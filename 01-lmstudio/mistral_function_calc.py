import json

import requests


# External function (tool) definition
def calculate(expression):
    try:
        print("Calculating expression: ", expression)
        result = eval(expression, {"__builtins__": {}}, {})
        result = str(result)

        print("Expression \"", expression, "\" result: " + result)

        return result
    except Exception as e:
        return f"Error: {e}"


# Call LM Studio and optionally handle function call
def call_mistral_with_function_call(prompt):
    url = "http://localhost:1234/v1/chat/completions"

    headers = {
        "Content-Type": "application/json"
    }

    tools = [
        {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Evaluate a simple math expression",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Math expression like '2 + 2 * (3 + 1)'"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }
    ]

    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools when needed."},
        {"role": "user", "content": prompt}
    ]

    payload = {
        "model": "mistralai/mistral-7b-instruct-v0.3",
        "messages": messages,
        "tools": tools,
        "tool_choice": "auto",
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    print("LM response: ", data)

    choice = data['choices'][0]
    tool_call = choice.get('tool_calls', [None])[0]

    # If model chooses to call function
    if tool_call:
        tool_name = tool_call["function"]["name"]
        tool_args = json.loads(tool_call["function"]["arguments"])

        if tool_name == "calculate":
            result = calculate(tool_args["expression"])

            # Return result as assistant message
            messages.append({
                "role": "assistant",
                "tool_calls": [tool_call]
            })
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call["id"],
                "name": "calculate",
                "content": result
            })

            # Re-run to let model respond with final answer
            payload["messages"] = messages
            response2 = requests.post(url, headers=headers, json=payload)
            final_content = response2.json()["choices"][0]["message"]["content"]
            return final_content.strip()

    # Otherwise, just return normal assistant message
    print("choice", choice)

    if (choice.get("finish_reason") == "tool_calls"):
        print("Request to LLM completed OK, tool call")
        message = choice["message"]
        if message is not None:
            tool_calls = message["tool_calls"]
            for tool_call in tool_calls:
                print("processing tool call: ", tool_call)
                function = None

                if tool_call["type"] == "function" and tool_call["function"] is not None:
                    function = tool_call["function"]

                if function is not None:
                    print("Processing function: ", function)
                    tool_name = function["name"]
                    tool_args = json.loads(function["arguments"])
                    tool_call_id = tool_call["id"]

                    print(f"Tool call id={tool_call_id} detected: {tool_name}({tool_args})")

                    #  Call the actual local function
                    if tool_name == "calculate":
                        result = calculate(tool_args["expression"])

                        # Send the result back to LM Studio as tool output
                        messages.append({
                            "role": "assistant",
                            "tool_calls": [tool_call]
                        })
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call_id,
                            "name": tool_name,
                            "content": result
                        })

                        # Final call to LM Studio with full context
                        payload["messages"] = messages
                        final_response = requests.post(url, headers=headers, json=payload)
                        final_answer = final_response.json()["choices"][0]["message"]["content"]

                        return final_answer.strip()
    else:
        # If no tool call, just return normal assistant message
        return choice["message"]["content"].strip()


# Example usage
if __name__ == "__main__":
    prompt = "What's the result of (5 + 3) * 4?"

    result = call_mistral_with_function_call(prompt)

    print("Mistral Response:\n", result)

    prompt = "What's the result of (12 + 8) / 4?"

    result = call_mistral_with_function_call(prompt)

    print("Mistral Response:\n", result)
