"""Channel 基类：定义统一接口 + 通用 HTTP POST + 简单限流。

每个通道 adapter 继承 Channel，覆盖 render_text / render_card / render_file，
实现"统一 Message → 该通道原生 payload"的映射；发送与凭据解析由基类统一处理。
"""
import json
import time
import urllib.error
import urllib.request


class Channel:
    name = ""            # 通道名（CLI 用，如 feishu）
    label = ""           # 中文显示名
    rate_per_min = 60    # 限流：每分钟最大发送数

    def __init__(self, config: dict):
        self.config = config or {}
        self._last_send = 0.0

    # ---------------- 子类覆盖 ----------------
    def render_text(self, message: dict) -> dict:
        raise NotImplementedError

    def render_card(self, message: dict) -> dict:
        raise NotImplementedError

    def render_file(self, message: dict) -> dict:
        # 默认降级：文件 → 文本说明（邮件/Telegram 会覆盖实现真附件）
        return self.render_text({"kind": "text", "text": f"[文件] {message.get('path', '')}"})

    # ---------------- 统一分派 ----------------
    def render(self, message: dict) -> dict:
        kind = message.get("kind")
        if kind == "text":
            return self.render_text(message)
        if kind == "card":
            return self.render_card(message)
        if kind == "file":
            return self.render_file(message)
        raise ValueError(f"通道 {self.name} 不支持消息类型 {kind}")

    # ---------------- 凭据解析 ----------------
    def resolve_target(self, target) -> dict:
        """从配置里取指定 target 的凭据；target=None 用默认目标。"""
        targets = self.config.get("targets", {})
        if target is None:
            target = self.config.get("default")
        if not target:
            raise ValueError(f"通道 {self.label} 未指定目标，且无默认目标")
        t = targets.get(target)
        if t is None:
            raise ValueError(f"通道 {self.label} 未找到目标「{target}」，已配置：{', '.join(targets) or '(空)'}")
        return t

    # ---------------- 发送 ----------------
    def send(self, message: dict, target=None) -> dict:
        payload = self.render(message)
        return self.post(target, payload)

    def post(self, target, payload: dict) -> dict:
        """由子类覆盖：真正把 payload 发到 target，返回 {ok, code, msg}。"""
        raise NotImplementedError

    # ---------------- 通用工具 ----------------
    def http_json(self, url: str, payload: dict, headers: dict = None) -> dict:
        """通用 JSON POST，带简单限流。"""
        self._throttle()
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        h = {"Content-Type": "application/json"}
        if headers:
            h.update(headers)
        req = urllib.request.Request(url, data=data, headers=h, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return {"ok": True, "code": 0, "body": json.loads(resp.read().decode("utf-8"))}
        except urllib.error.HTTPError as e:
            return {"ok": False, "code": e.code, "body": e.read().decode("utf-8", "ignore")}
        except Exception as e:
            return {"ok": False, "code": -1, "body": str(e)}

    def _throttle(self):
        interval = 60.0 / self.rate_per_min
        wait = interval - (time.time() - self._last_send)
        if wait > 0:
            time.sleep(wait)
        self._last_send = time.time()
