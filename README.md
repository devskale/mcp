MCPSimpleAPI

implement a simple MCP Server that queries an API and returns the response

keep track of the goal, todos, status and achievements in README.md

## Goal
Create a simple MCP (Model Context Protocol) server using FastMCP in Python that queries a news API and returns the response in a structured format.

## Todos
- [x] Set up the basic MCP server structure with FastMCP.
- [x] Implement a tool to query the news API with a given topic.
- [ ] Test the server locally to ensure API requests are handled correctly.
- [x] Implement a tool to fetch content from a given URL.
- [ ] Document usage instructions for running the server and integrating with MCP-capable IDEs.

## Status
- The server implementation is complete with tools to fetch news articles based on a topic and to fetch content from a specified URL.
- The server queries API endpoints `https://amd1.mooo.com/api/duck/news` and `https://amd1.mooo.com/api/w3m` using an authorization token loaded from environment variables for security.

## Achievements
- Successfully created `server.py` with FastMCP to define the SimpleAPI server.
- Implemented `fetch_news` tool to make API calls and return JSON responses.
- Implemented `fetch_url` tool to fetch content from a given URL using the w3m API.
- Added version information as a resource accessible via `info://api_version`.
- Updated authorization method to use environment variables for enhanced security.

## Example API Call (fetch_news)
```bash
curl -X 'GET' \
  'https://amd1.mooo.com/api/duck/news?topic=elon%20musk' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer test23'
```

## Example API Call (fetch_url)
```bash
curl -X 'GET' \
  'https://amd1.mooo.com/api/w3m?url=https%3A%2F%2Forf.at' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer test23'
```

## Example Response
```json
{
  "results": [
    {
      "date": "2025-07-08T12:52:00+00:00",
      "title": "Tesla investors have a very clear message for Elon Musk: Stay away from politics",
      "body": "One analyst called on Tesla's board of directors to act and set \"ground rules\" for Musk's political involvements.",
      "url": "https://www.businessinsider.com/tesla-investors-message-for-elon-musk-stay-away-from-politics-2025-7",
      "image": "https://i.insider.com/686b2fe685e81483682d7026?width=1200&format=jpeg",
      "source": "Insider"
    },
    {
      "date": "2025-07-08T09:02:00+00:00",
      "title": "Elon Musk's new US political party faces steep challenges",
      "body": "Musk described his new party on his platform X as tech-centric, budget-conscious, pro-energy and centrist, with the goal of drawing both disaffected Democrats and Republicans. Musk has criticized the tax-cut bill, which is forecast to add about $3.4 trillion to the United States' debt.",
      "url": "https://www.reuters.com/world/us/musk-faces-daunting-path-challenging-us-two-party-system-2025-07-08/",
      "image": "https://www.reuters.com/resizer/v2/B3TF4VHQRJMK3KJP3Z3MA4TLGI.jpg?auth=284014372c7853361961929f77d56134ee2e1a625508b74fef153336d047642e&height=1005&width=1920&quality=80&smart=true",
      "source": "Reuters"
    },
    ...
  ]
}
```

## MCP Server Configuration
To integrate the `simple-web-api` server with your MCP-capable IDE or agent, add the following configuration to your settings:

```json
"simple-web-api": {
  "disabled": false,
  "timeout": 60,
  "type": "stdio",
  "command": "python",
  "args": [
    "C:\\Users\\Hans\\code\\agentic\\mymcps\\mcp_buildflow\\server.py"
  ]
}
```
