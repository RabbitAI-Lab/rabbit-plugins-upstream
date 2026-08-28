"""LLM + MCP 客户端：把用户问题交给大模型，由大模型决定调用哪些 MCP 工具，
再通过 MCP 协议(stdio JSON-RPC)把工具结果回传给大模型，循环直到得到最终答案。

按作业要求，内置三种"构建方式不同"的模型后端，用于对比它们之间的差异：
  openai    : OpenAI 官方接口（function calling）
  deepseek  : DeepSeek（OpenAI 兼容协议，function calling）
  anthropic : Claude（独立的 tool_use 协议，格式与 OpenAI 不同）

用法：
  python llm_client.py --provider openai --model gpt-4o
  python llm_client.py --provider deepseek --model deepseek-chat
  python llm_client.py --provider anthropic --model claude-sonnet-4-6
  python llm_client.py --provider openai --verbose   # 打印工具调用链路
"""
import asyncio
import json
import os
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

SERVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ecommerce_server.py")

DEFAULT_MODELS = {
    "openai": "gpt-4o",
    "deepseek": "deepseek-chat",
    "anthropic": "claude-sonnet-4-6",
}
BASE_URLS = {
    "openai": None,
    "deepseek": "https://api.deepseek.com",
    "anthropic": None,
}

MAX_TURNS = 15

SYSTEM_PROMPT = """你是电商碳排分析助手，可通过工具查询商品、BOM 构成、单品详情与运费。

计算规则：
1. 先用 search_product 找到目标商品 id；
2. 用 get_product_structure 获取该商品 BOM（子件构成）；
3. 对每个子件用 get_item_details 获取重量/成本/碳排，按数量相乘累加；
4. 商品本身（如礼盒）也有独立的重量/成本/碳排，属于包装，需一并计入；
5. 用 calculate_shipping 按仓库、目的地、总重量计算运费与运输碳排；
6. 最终给出：总重量(kg)、总成本(元，含运费)、总碳排放(kg CO2，含运输碳排)。
请逐步调用工具，展示计算过程后给出最终答案。"""


class ToolCall:
    def __init__(self, id, name, arguments):
        self.id = id
        self.name = name
        self.arguments = arguments


class ChatTurn:
    def __init__(self, text, tool_calls):
        self.text = text
        self.tool_calls = tool_calls


# ---- 后端 1/2：OpenAI / DeepSeek（同为 function calling，仅 base_url 不同） ----
class OpenAIProvider:
    def __init__(self, model, api_key, base_url=None):
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def tools_from_mcp(self, mcp_tools):
        return [
            {
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.inputSchema,
                },
            }
            for t in mcp_tools
        ]

    def init_messages(self, system, user):
        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]

    def add_assistant_tool_calls(self, messages, calls):
        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": c.id,
                    "type": "function",
                    "function": {"name": c.name, "arguments": json.dumps(c.arguments, ensure_ascii=False)},
                }
                for c in calls
            ],
        })

    def add_tool_results(self, messages, results):
        for call, output in results:
            messages.append({"role": "tool", "tool_call_id": call.id, "content": output})

    async def chat(self, messages, tools):
        resp = await self.client.chat.completions.create(
            model=self.model, messages=messages, tools=tools
        )
        msg = resp.choices[0].message
        calls = [
            ToolCall(tc.id, tc.function.name, json.loads(tc.function.arguments or "{}"))
            for tc in (msg.tool_calls or [])
        ]
        return ChatTurn(msg.content or "", calls)


# ---- 后端 3：Anthropic Claude（独立的 tool_use 协议） ----
class AnthropicProvider:
    def __init__(self, model, api_key):
        from anthropic import AsyncAnthropic
        self.client = AsyncAnthropic(api_key=api_key)
        self.model = model
        self.system = ""

    def tools_from_mcp(self, mcp_tools):
        return [
            {"name": t.name, "description": t.description, "input_schema": t.inputSchema}
            for t in mcp_tools
        ]

    def init_messages(self, system, user):
        self.system = system
        return [{"role": "user", "content": user}]

    def add_assistant_tool_calls(self, messages, calls):
        messages.append({
            "role": "assistant",
            "content": [
                {"type": "tool_use", "id": c.id, "name": c.name, "input": c.arguments}
                for c in calls
            ],
        })

    def add_tool_results(self, messages, results):
        messages.append({
            "role": "user",
            "content": [
                {"type": "tool_result", "tool_use_id": call.id, "content": output}
                for call, output in results
            ],
        })

    async def chat(self, messages, tools):
        resp = await self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.system,
            messages=messages,
            tools=tools,
        )
        text = "".join(b.text for b in resp.content if b.type == "text")
        calls = [ToolCall(b.id, b.name, b.input) for b in resp.content if b.type == "tool_use"]
        return ChatTurn(text, calls)


def make_provider(name, model):
    api_key = os.getenv(f"{name.upper()}_API_KEY")
    if not api_key:
        raise SystemExit(f"缺少 {name.upper()}_API_KEY，请在 .env 或环境变量中配置")
    if name in ("openai", "deepseek"):
        return OpenAIProvider(model, api_key, base_url=BASE_URLS[name])
    return AnthropicProvider(model, api_key)


def extract_text(result):
    sc = result.structuredContent
    if sc and isinstance(sc, dict) and "result" in sc:
        return json.dumps(sc["result"], ensure_ascii=False)
    parts = [getattr(c, "text", None) for c in result.content]
    return "\n".join(p for p in parts if p is not None)


async def run(provider_name, model, question, verbose):
    provider = make_provider(provider_name, model)
    params = StdioServerParameters(command=sys.executable, args=[SERVER_PATH])

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            mcp_tools = (await session.list_tools()).tools
            if verbose:
                print(f"[mcp] 发现工具: {[t.name for t in mcp_tools]}")

            tools = provider.tools_from_mcp(mcp_tools)
            messages = provider.init_messages(SYSTEM_PROMPT, question)

            for _ in range(MAX_TURNS):
                turn = await provider.chat(messages, tools)
                if not turn.tool_calls:
                    return turn.text

                provider.add_assistant_tool_calls(messages, turn.tool_calls)
                results = []
                for call in turn.tool_calls:
                    mcp_result = await session.call_tool(call.name, call.arguments)
                    output = extract_text(mcp_result)
                    if verbose:
                        print(f"[tool] {call.name}({json.dumps(call.arguments, ensure_ascii=False)}) -> {output}")
                    results.append((call, output))
                provider.add_tool_results(messages, results)

            return "达到最大轮次仍未得到最终答案"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="LLM + MCP 电商碳排分析")
    parser.add_argument("--provider", choices=["openai", "deepseek", "anthropic"], default="openai")
    parser.add_argument("--model", default=None, help="模型名，缺省按 provider 选默认值")
    parser.add_argument("--question", default="我打算给北京的客户发10套'红酒礼盒'。请帮我算一下总重量、总成本和总碳排放是多少？")
    parser.add_argument("--verbose", action="store_true", help="打印工具调用链路")
    args = parser.parse_args()

    model = args.model or DEFAULT_MODELS[args.provider]
    print(f"[model] provider={args.provider}, model={model}")
    answer = asyncio.run(run(args.provider, model, args.question, args.verbose))
    print("\n===== 最终答案 =====\n")
    print(answer)


if __name__ == "__main__":
    main()
