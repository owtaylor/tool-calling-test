import json
import requests

PROMPT="""\
<|start_of_role|>system<|end_of_role|>Knowledge Cutoff Date: April 2024.
Today's Date: February 19, 2025.
You are Granite, developed by IBM. You are a helpful AI assistant with access to the following tools. When a tool is required to answer the user's query, respond with <|tool_call|> followed by a JSON list of tools used. If a tool does not exist in the provided list of tools, notify the user that you do not have the ability to fulfill the request.<|end_of_text|>
<|start_of_role|>tools<|end_of_role|>[
    {
        "name": "get_current_weather",
        "description": "Get the current weather",
        "arguments": {
            "location": {
                "description": "The city and state, e.g. San Francisco, CA"
            }
        }
    },
    {
        "name": "get_stock_price",
        "description": "Retrieves the current stock price for a given ticker symbol. The ticker symbol must be a valid symbol for a publicly traded company on a major US stock exchange like NYSE or NASDAQ. The tool will return the latest trade price in USD. It should be used when the user asks about the current or most recent price of a specific stock. It will not provide any other information about the stock or company.",
        "arguments": {
            "ticker": {
                "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
            }
        }
    },
    {
        "name": "builtin_read_file",
        "description": ""Use this tool if you need to view the contents of an existing file.",
        "arguments": {
            "filepath": {
                "description": " "The path of the file to read, relative to the root of the workspace (NOT uri or absolute path)"The city and state, e.g. San Francisco, CA"
            }
        }
    }
]<|end_of_text|>
<|start_of_role|>user<|end_of_role|>what does "test.js" file do?<|end_of_text|>
"""

response = requests.post("http://localhost:11434/api/generate", json={
        "model": "granite3.2:8b",
        "prompt": PROMPT,
        "raw": True,
        "stream": False,
        "options": {
            "temperature": 0.1,
        }
    })
print(json.dumps(response.json(), indent=2))


