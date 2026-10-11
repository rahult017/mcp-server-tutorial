# client.py
import asyncio
from mcp import Client


async def main() -> None:
    name = input("Enter your name: ").strip()
    a = int(input("Enter the first number: ").strip())
    b = int(input("Enter the second number: ").strip())

    async with Client("http://127.0.0.1:8000/mcp") as client:
        # Call hello_world tool
        result = await client.call_tool(
            "hello_world",
            {"name": name},
        )
        print("hello_world →", result.structured_content)

        # Call add tool
        total = await client.call_tool(
            "add_numbers",
            {"a": a, "b": b},
        )
        print("add →", total.structured_content)


if __name__ == "__main__":
    asyncio.run(main())