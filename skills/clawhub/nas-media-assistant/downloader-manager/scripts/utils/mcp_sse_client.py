"""MCP-over-SSE 客户端。

封装 MCP SSE 协议: 建立 SSE 会话 -> initialize 握手 -> tools/call 调用。
支持会话复用（多次 tool call 共享一个 SSE 连接）和自动重连。

用法:
    client = McpSseClient("https://api-xmodels.xunlei.com/models/sse/<key>")
    client.connect()
    result = client.call_tool("xunlei_download_list_device", {})
    client.disconnect()
"""
from __future__ import annotations
import json
import threading
import time
import logging
from typing import Any, Optional

import requests

logger = logging.getLogger("mcp_sse")

_JSONRPC_VERSION = "2.0"
_PROTOCOL_VERSION = "2024-11-05"
_CALL_TIMEOUT = 30          # 单次 tool call 等待响应秒数
_IDLE_TIMEOUT = 120         # 会话空闲超时自动断开


class McpSseError(Exception):
    """MCP 调用异常。"""


class McpSseClient:
    """MCP SSE 客户端：会话管理 + JSON-RPC 请求/响应。"""

    def __init__(self, sse_url: str, call_timeout: int = _CALL_TIMEOUT):
        self.sse_url = sse_url
        self.call_timeout = call_timeout
        self._base = sse_url.rsplit("/", 1)[0].rsplit("/models", 1)[0]
        self._endpoint: Optional[str] = None
        self._next_id = 1
        self._responses: dict[int, Any] = {}
        self._errors: list[str] = []
        self._sse_thread: Optional[threading.Thread] = None
        self._stop = threading.Event()
        self._connected = False
        self._lock = threading.Lock()

    # ---- SSE 监听线程 ----

    def _sse_loop(self):
        """后台线程: 持续监听 SSE 流，按 id 收集响应。"""
        data_buf: list[str] = []
        try:
            with requests.get(
                self.sse_url, stream=True, timeout=300,
                headers={"Accept": "text/event-stream"},
            ) as r:
                for raw in r.iter_lines():
                    if self._stop.is_set():
                        break
                    if raw is None:
                        continue
                    line = raw.decode("utf-8", "replace") if isinstance(raw, bytes) else raw
                    if line == "":
                        if data_buf:
                            data = "\n".join(data_buf)
                            data_buf.clear()
                            self._dispatch(data)
                        continue
                    if line.startswith("data: "):
                        data_buf.append(line[6:])
                    elif line.startswith("data:"):
                        data_buf.append(line[5:])
        except Exception as e:
            if not self._stop.is_set():
                self._errors.append(str(e))
                logger.warning("SSE 流异常: %s", e)
        finally:
            self._connected = False

    def _dispatch(self, data: str):
        """处理一条 SSE data 事件。"""
        if data.startswith("/"):
            self._endpoint = self._base + data
            return
        try:
            msg = json.loads(data)
        except json.JSONDecodeError:
            logger.debug("非 JSON SSE 数据: %s", data[:100])
            return
        rid = msg.get("id")
        if rid is not None:
            self._responses[rid] = msg
        elif "error" in msg:
            self._errors.append(json.dumps(msg.get("error"), ensure_ascii=False))

    # ---- 公共 API ----

    def connect(self) -> bool:
        """建立 SSE 会话并完成 initialize 握手。"""
        self._stop.clear()
        self._responses.clear()
        self._errors.clear()
        self._sse_thread = threading.Thread(target=self._sse_loop, daemon=True)
        self._sse_thread.start()
        # 等待 endpoint 事件
        deadline = time.time() + 10
        while time.time() < deadline:
            if self._endpoint:
                break
            if self._errors:
                break
            time.sleep(0.2)
        if not self._endpoint:
            logger.error("未收到 SSE endpoint 事件; errors=%s", self._errors)
            return False
        # initialize 握手
        resp = self._post({
            "jsonrpc": _JSONRPC_VERSION, "id": self._next_id,
            "method": "initialize",
            "params": {
                "protocolVersion": _PROTOCOL_VERSION,
                "capabilities": {},
                "clientInfo": {"name": "nas-media-assistant", "version": "1.0"},
            },
        })
        self._next_id += 1
        if not resp:
            # 等待 SSE 响应
            resp = self._wait_response(self._next_id - 1, 10)
        if not resp or "error" in resp:
            logger.error("initialize 失败: %s", resp)
            return False
        # initialized 通知
        self._post({"jsonrpc": _JSONRPC_VERSION, "method": "notifications/initialized"})
        time.sleep(1)
        self._connected = True
        logger.info("MCP SSE 会话已建立: %s", self._endpoint[:60])
        return True

    def call_tool(self, name: str, arguments: dict | None = None) -> Any:
        """调用 MCP tool，返回 result.content。"""
        if not self._connected and not self.connect():
            raise McpSseError("SSE 会话未建立")
        rid = self._next_id
        self._next_id += 1
        self._post({
            "jsonrpc": _JSONRPC_VERSION, "id": rid,
            "method": "tools/call",
            "params": {"name": name, "arguments": arguments or {}},
        })
        resp = self._wait_response(rid, self.call_timeout)
        if not resp:
            raise McpSseError(f"tool '{name}' 超时无响应")
        if "error" in resp:
            err = resp["error"]
            raise McpSseError(f"tool '{name}' 返回错误: {err.get('message', err)}")
        result = resp.get("result", {})
        # MCP 返回 content 数组，提取文本
        content = result.get("content", [])
        texts = []
        for c in content:
            if c.get("type") == "text":
                texts.append(c["text"])
        raw = "\n".join(texts) if texts else json.dumps(result, ensure_ascii=False)
        # 尝试 JSON 解析
        try:
            return json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            return raw

    def list_tools(self) -> list[dict]:
        """获取工具列表。"""
        if not self._connected and not self.connect():
            raise McpSseError("SSE 会话未建立")
        rid = self._next_id
        self._next_id += 1
        self._post({
            "jsonrpc": _JSONRPC_VERSION, "id": rid,
            "method": "tools/list", "params": {},
        })
        resp = self._wait_response(rid, self.call_timeout)
        if not resp:
            raise McpSseError("tools/list 超时")
        return resp.get("result", {}).get("tools", [])

    def disconnect(self):
        """断开会话。"""
        self._stop.set()
        self._connected = False
        self._endpoint = None

    @property
    def connected(self) -> bool:
        return self._connected

    # ---- 内部方法 ----

    def _post(self, payload: dict) -> dict | None:
        """POST JSON-RPC 到 message endpoint，返回 HTTP 响应体（可能为空）。"""
        if not self._endpoint:
            return None
        try:
            r = requests.post(self._endpoint, json=payload, timeout=15)
            if r.status_code == 202:
                return {}
            try:
                return r.json()
            except Exception:
                return {}
        except requests.RequestException as e:
            logger.warning("POST 失败: %s", e)
            return None

    def _wait_response(self, rid: int, timeout: int) -> dict | None:
        """轮询等待指定 id 的 SSE 响应。"""
        deadline = time.time() + timeout
        while time.time() < deadline:
            if rid in self._responses:
                return self._responses.pop(rid)
            if not self._sse_thread or not self._sse_thread.is_alive():
                # SSE 断开，尝试重连
                logger.warning("SSE 线程已终止，尝试重连...")
                if self.connect():
                    # 重连后重新发送请求
                    continue
                break
            time.sleep(0.3)
        return self._responses.pop(rid, None)
