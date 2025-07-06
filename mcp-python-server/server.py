from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP('Python-MCP-Server')
print("MCP Python server starting...", flush=True)
@mcp.tool()
def get_info_about(name: str) -> str:
    employee_info = {
        "name": "Ayoub",
        "salary": 10000,
    }
    return json.dumps(employee_info)

app = mcp.sse_app  # adjust this line based on your FastMCP
