from mcp.server.fastmcp import FastMCP
import json

mcp = FastMCP('Python-MCP-Server')

@mcp.tool()
def get_info_about(name: str) -> str:
    employee_info = {
        "name": "Badr",
        "salary": 75500,
    }
    return json.dumps(employee_info)

def main():
    print("Starting mcp-python-server...")
    mcp.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
