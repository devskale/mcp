## goal
lets create simple coding guideline to develop a MCP (model context protocol) server.
## framework
- python
- fastmcp
    - The fast, Pythonic way to build MCP servers and clients
    - github: jlowin/fastmcp



# Coding Guidelines for MCP Server with FastMCP
===========================================================

This document provides a concise set of guidelines for developing a simple MCP (Model Context Protocol) server using FastMCP in Python, focusing on essential practices for clarity and maintainability.

**1. Project Structure**  
- Use `server.py` as the main file for your FastMCP server.  
- For larger projects, organize tools in a `tools/` directory and resources in a `resources/` directory.

**2. Naming Conventions**  
- Name the server instance to reflect its purpose (e.g., `mcp = FastMCP("MathHelper")`).  
- Use action-oriented names for tools (e.g., `calculate_sum`).  
- Name resources to indicate exposed data (e.g., `user_profile`).

**3. Defining Tools**  
- Mark functions as tools with `@mcp.tool`.  
- Use type hints for parameters and return values.  
- Write clear docstrings and keep tools focused on a single task.  
  Example:
  ```python
  @mcp.tool
  def calculate_sum(a: int, b: int) -> int:
      """Calculate sum of two integers."""
      return a + b
  ```

**4. Exposing Resources**  
- Use `@mcp.resource` with meaningful URIs (e.g., `info://server_version`).  
- Return structured data like dictionaries.  
  Example:
  ```python
  @mcp.resource("info://server_version")
  def get_server_version():
      """Return server version."""
      return "1.0.0"
  ```

**5. Error Handling**  
- Validate inputs and raise descriptive exceptions.  
- Use try-except for operations prone to failure.

**6. Running the Server**  
- Add `if __name__ == "__main__": mcp.run()` to `server.py`.  
- Run locally with `fastmcp run server.py` for development.

**7. Documentation**  
- Include detailed docstrings for tools and resources.  
- Add comments for complex logic or a README for server overview.

**8. Simple MCP Server Example**  
```python
from fastmcp import FastMCP
mcp = FastMCP("SimpleCalculator")

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("info://calculator_version")
def get_calculator_version():
    """Return server version."""
    return "1.0.0"

if __name__ == "__main__":
    mcp.run()
```

**9. IDE Integration (Claude Desktop with FastMCP)**  
- **Purpose**: Extend a MCP capable IDE or Agent's apabilities with custom MCP tools and resources.  
- **Local Setup**: Use STDIO transport for local servers. 
- **Dependencies**: Specify with `--with` flag (e.g., `--with pandas`) or in server code. Requires `uv` in system PATH for dependency management.  
- **Environment Variables**: Pass explicitly (e.g., `--env-var API_KEY=your-key`) as servers run in isolated environments.  
- **Manual Configuration**: Edit JSON config at `%APPDATA%\Claude\claude_desktop_config.json` (Windows) or equivalent. Example:
  ```json
  {
    "mcpServers": {
      "dice-roller": {
        "command": "python",
        "args": ["path/to/server.py"]
      }
    }
  }
  ```

This summary captures the core practices for creating a simple MCP server with FastMCP and integrating it with Claude Desktop. For further details on contributing to FastMCP or advanced configurations, refer to the original documentation.
