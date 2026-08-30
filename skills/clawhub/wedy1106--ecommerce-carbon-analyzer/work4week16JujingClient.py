import asyncio
import json
import os

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import OpenAI


def convert_mcp_to_openai_tools(mcp_tools):
    """将 MCP 工具格式转换为 OpenAI 兼容的 Function Calling 格式"""
    openai_tools = []
    for tool in mcp_tools:
        openai_tools.append({
            "type": "function",
            "function": {
                "name": tool.name,
                "description": tool.description or f"Tool: {tool.name}",
                "parameters": tool.input_schema,
            },
        })
    return openai_tools

async def run_agent(model_name: str = "Pro/deepseek-ai/DeepSeek-V3.2", system_content = "", user_content = ""):
    # 配置 MCP Server 启动参数
    os.environ['SILICONFLOW_API_KEY'] = ''
    server_params = StdioServerParameters(
        command="python",
        args=[os.path.join(os.path.dirname(__file__), "work4week16JujingServer.py")],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # 1. 获取 MCP Server 提供的工具
            mcp_tools = await session.list_tools()
            openai_tools = convert_mcp_to_openai_tools(mcp_tools.tools)

            # 2. 初始化 LLM 客户端
            llm_client = OpenAI(
                api_key=os.getenv('SILICONFLOW_API_KEY'),
                base_url="https://api.siliconflow.cn/v1",
            )

            messages = [
                {
                    "role": "system",
                    "content": system_content
                },
                {
                    "role": "user",
                    "content": user_content
                }
            ]

            print(f"--- 使用模型: {model_name} ---\n")

            # ========== 多轮对话交互 ==========
            max_rounds = 10  # 防止死循环
            for round_num in range(1, max_rounds + 1):
                print(f"\n{'=' * 50}")
                print(f"--- 第 {round_num} 轮对话 ---")
                print(f"{'=' * 50}")

                # 调用 LLM
                response = llm_client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    tools=openai_tools,
                    tool_choice="auto"
                )

                message = response.choices[0].message
                print(f"LLM 对话回答：: {message.content[:100]}")
                messages.append(message)

                # 如果 LLM 没有调用工具，说明它给出了最终答案
                if not message.tool_calls:
                    print("\n=== 最终计算结果 ===")
                    print(message.content)
                    break

                # 执行所有工具调用
                print(f"LLM 请求调用 {len(message.tool_calls)} 个工具:")
                for tc in message.tool_calls:
                    func_name = tc.function.name
                    func_args = json.loads(tc.function.arguments)

                    print(f"  → {func_name}({func_args})")

                    # 通过 MCP 调用 Server 端工具
                    result = await session.call_tool(func_name, func_args)
                    tool_content = result.content[0].text if result.content else "{}"

                    print(f"  ← 返回: {tool_content[:100]}..." if len(
                        tool_content) > 100 else f"  ← 返回: {tool_content}")

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": tool_content
                    })
            else:
                print("⚠️ 达到最大轮次限制，强制结束")


if __name__ == "__main__":
    asyncio.run(run_agent(model_name="Pro/deepseek-ai/DeepSeek-V3.2", system_content="你是一个专业的电商物流分析师。你需要使用提供的工具来回答用户的问题。对于计算总重量、总成本和总碳排放，请逐步调用工具：先搜索商品，再获取BOM和详情，最后计算运费。", user_content="我打算给北京的客户发10套'红酒礼盒'。请帮我算一下总重量、总成本和总碳排放是多少？"))