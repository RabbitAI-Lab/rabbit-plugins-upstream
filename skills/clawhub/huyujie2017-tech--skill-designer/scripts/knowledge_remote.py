#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""knowledge_remote.py — 远程知识服务后端（**衔接位**：阶段1 预留契约，阶段2 才实现服务端）

这个文件存在的唯一理由
────────────────────────────────────────────────────────────────────
skill-designer 的终局形态是 **「本地基础版 + 远程增强服务」**（ADR-001 目标 2）：

    本地（永久离线完备 I1）          远程（增强 · 可失败）
    ───────────────────────         ───────────────────────────────
    流程内核 / 门禁 / 错误码          历史全量条目全文（低频大件）
    条目索引（机器件 + 上下文件）      外部样本库与历史档案全文
    高频条目全文（离线兜底包）        更新订阅（每轮吸收的新条目推送）
    失败处理与可触线规则              增强检索（语义补召回 / 跨版本对比 / 自定义标签）

而「远程增强」要收钱（SkillHub Pay）。**计费改造由 `skill-paid` 那条流程单独做**，
所以本文件现在**不实现服务端**，只把三件事钉死，让将来改造**不必回头改主流程**：

  ① **同签名后端协议**：`index / get / search / verify` 与 LocalBackend 完全一致
     —— 主流程一行不改即可切后端；`--backend auto` 就是「远程优先 + 本地兜底」。
  ② **支付契约的对接点**：`pay_hook()` 是唯一的注入位。默认实现只**打印指引并熔断**；
     skill-paid 改造时替换它即可（HTTP 402 + `WeixinPay-Required` + `X-Out-Trade-No` 重试）。
  ③ **熔断语义**（DP-210 失败即熔断，不得向右兜底）：
     远程不可用 → 用**本地同版本**继续；本地也没有该条目 → **报缺口 + 给可执行动作**；
     **绝不用模型记忆补**（那会产出"看起来成功的错误答案"，比报错危险得多）。

与 skill-paid 的契约对齐（读 `skill-paid` 后的实测结论）
────────────────────────────────────────────────────────────────────
  · 触发标识返回方式（CLI 输出 / HTTP Header）与 notify_url 是**两条平行线**，不可混。
    本后端走 **HTTP Header** 形态（`WeixinPay-Required`），与 skill-paid 的 server 模板一致。
  · 支付后重试凭 **`X-Out-Trade-No`** 头（Body 与首次一致）——本后端把它固化为常量。
  · **四把凭证归属**：本地主链路只用「商户 API 证书私钥 + 序列号」；APIv3 密钥与平台公钥
    **只在回调侧被消耗**，且 **APIv3 密钥不参与 v3 签名**。故本文件**不读任何密钥明文**，
    只读**环境变量名**（`tokenEnv` / `payKeyEnv`），与 skill-paid「只写环境变量名」的红线一致。
  · **notify_url 必须是真实 HTTPS**，不得填 `example.com` 占位（skill-paid M16）。

依赖与离线
────────────────────────────────────────────────────────────────────
  仅标准库（urllib）。**未配置远程时本模块不产生任何网络请求**，纯本地流程不受影响（I1）。

用法
────────────────────────────────────────────────────────────────────
    sd_cli knowledge get D-133 --backend remote    # 走远程（未配置 → E014 + 给动作）
    sd_cli knowledge search --text 路由 --backend auto   # 远程优先，失败回落本地
    sd_cli knowledge index --backend remote --write      # 拉远程 manifest（可离线缓存）
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

# ─────────────────────────── 契约常量（勿改名，skill-paid 依赖） ───────────────────────────

HEADER_PAY_REQUIRED = "WeixinPay-Required"      # 首次请求：服务端返回 HTTP 402 + 此头
HEADER_OUT_TRADE_NO = "X-Out-Trade-No"          # 支付后重试：客户端带此头
HTTP_PAY_REQUIRED = 402                          # 支付所需的 HTTP 状态码

DEFAULT_BASE_URL_ENV = "KNOWLEDGE_REMOTE_URL"     # 只存**环境变量名**，本地不落 URL 明文
DEFAULT_TOKEN_ENV = "KNOWLEDGE_REMOTE_TOKEN"      # 平台注入的短时 token（ADR §10.1 V2）
DEFAULT_PAY_KEY_ENV = "SKILLHUB_RSA_PRIVATE_KEY"  # 仅供将来注入的支付钩子读取；本模块不自用
DEFAULT_TIMEOUT = 8
MAX_RETRY = 1        # **硬上限**（对齐可触线规则：任何重试类纪律必须带数字上限）


class RemoteNotConfigured(RuntimeError):
    """未配置远程服务 —— 属**正常状态**（免费层用户就是这种），不是故障。"""


class RemoteUnavailable(RuntimeError):
    """远程不可用（超时 / 5xx / 解析失败）。→ 熔断，不重试超过 MAX_RETRY 次。"""


class RemoteIntegrityError(RuntimeError):
    """远程返回的正文与其 hash 不符 —— 远端可能被篡改 / 缓存脏。→ 拒绝使用。"""


class PayRequired(RuntimeError):
    """远程条目属付费层且尚未授权。→ 交给 `pay_hook`（skill-paid 的注入位）。"""

    def __init__(self, payment_code: str, out_trade_no: str, eid: str):
        super().__init__(f"{eid} 需要支付授权")
        self.payment_code = payment_code
        self.out_trade_no = out_trade_no
        self.eid = eid


class RemoteVersionTooOld(RuntimeError):
    """本地流程版本低于远程库要求（第四处一致性面）→ 熔断 + 升级指引。

    为什么不容忍「静默用旧流程跑新库」：新旧两侧对同一批条目 ID 的语义可能已变，
    旧流程读新库会产出**看起来正常但语义错位**的知识注入 —— 比直接报错危险得多（DP-210）。
    """


# ─────────────────────────── 配置与工具 ───────────────────────────

def load_remote_config(root: Path) -> dict:
    """读 library/remote_config.json（只有配置模板；真实地址/token 走环境变量）。"""
    p = root / "library" / "remote_config.json"
    if not p.is_file():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}


def local_flow_version(root: Path) -> str:
    """本地流程版本：唯一事实源是 `config.json` 的 `version`（勿另立字段，DP-204）。"""
    p = Path(root) / "config.json"
    if not p.is_file():
        return ""
    try:
        return str(json.loads(p.read_text(encoding="utf-8")).get("version", "")).strip()
    except (ValueError, OSError):
        return ""


def _vkey(v: str):
    return tuple(int(x) for x in re.findall(r"\d+", v or ""))


def check_flow_version(root: Path, cfg: dict | None = None) -> dict:
    """版本协商**启动校验**（ADR §7 措施 2.4）：本地流程 vs 远程声明的最低流程版本。

    这是**第四处一致性面**——前三是「条目 ID / manifest / 检索签名」。不设它，
    远程化之后必然复现「双落点漂移」：升级了库没升级流程，或反过来。

    返回 {"ok", "detail", "need", "have"}；不抛错，由调用方决定熔断还是仅告警。
    """
    cfg = cfg if cfg is not None else load_remote_config(root)
    need = str(cfg.get("versionNegotiation", {}).get("minFlowVersion", "")).strip()
    have = local_flow_version(root)
    if not need:
        return {"ok": True, "detail": "远程未声明 minFlowVersion（跳过协商）", "need": "", "have": have}
    if not have:
        return {"ok": False, "need": need, "have": have,
                "detail": "读不到本地流程版本（config.json 的 version）→ 先修发布包元数据"}
    if _vkey(have) < _vkey(need):
        return {"ok": False, "need": need, "have": have,
                "detail": f"本地流程 {have} < 远程库要求的 {need}"
                          f" → 请升级 skill-designer 本体；应急可用 `--backend local` 走本地全量"}
    return {"ok": True, "need": need, "have": have, "detail": f"流程 {have} ≥ 要求 {need}"}


def sha256_of(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def pay_hook(eid: str, payment_code: str, out_trade_no: str) -> int:
    """**支付触发钩子 —— 本文件唯一的注入位（衔接点）**。

    默认实现：**不自行支付**，只打印「怎么付」并返回未接管，交由上层熔断。
    为什么默认不实现：计费改造由 `skill-paid` 流程单独做（教授 2026-09-12 明确）；
    本模块的职责是**留好位置**，不是越权实现支付 —— 这也是 I3「知识不含行为指令」
    在代码侧的镜像：**能力的注入必须显式、单点、可审计**。

    skill-paid 改造时的替换契约（保持签名不变即可）：
        def pay_hook(eid, payment_code, out_trade_no) -> int:
            # 把 WeixinPay-Required 交给 runner（agent 侧会拉起支付卡片）
            # 支付完成后，调用方带 X-Out-Trade-No 重试
            return 0  # 0=已接管并成功；非 0=未接管（上层熔断）
    """
    print(f"💳 条目 {eid} 属远程付费层，需要支付授权。", file=sys.stderr)
    print(f"   支付标识（{HEADER_PAY_REQUIRED}）：{payment_code}", file=sys.stderr)
    print(f"   支付后凭 {HEADER_OUT_TRADE_NO}: {out_trade_no} 重试同一请求即可取回正文。", file=sys.stderr)
    print("   说明：本仓库**尚未接入计费**（改造由 skill-paid 流程单独进行）。"
          "当前可用替代动作：加 `--backend local` 用本地同版本条目。", file=sys.stderr)
    return 1        # 未接管 → 上层按熔断处理，**不静默降级**


# ─────────────────────────── 远程后端 ───────────────────────────

class RemoteBackend:
    """远程知识后端：与 LocalBackend **同签名**（index/get/search/verify）。

    设计要点：
      · **同签名**是硬要求——主流程只调一个门面，切换后端不该改主流程（ADR §5.2 契约③）。
      · 任何失败都**抛错而非返回空**：空结果会被上层的"没找到"逻辑吃掉，从而掩盖故障（DP-210）。
      · `offline_fallback` 只在 `auto` 模式下由门面传 True；`remote` 模式**绝不回落**。
    """

    def __init__(self, root: Path, config: dict | None = None, token: str | None = None):
        self.root = root
        self.cfg = config if config is not None else load_remote_config(root)
        base_env = self.cfg.get("baseUrlEnv", DEFAULT_BASE_URL_ENV)
        token_env = self.cfg.get("tokenEnv", DEFAULT_TOKEN_ENV)
        self.base = (os.environ.get(base_env) or "").rstrip("/")
        self.token = token or os.environ.get(token_env) or ""
        self.timeout = int(self.cfg.get("timeoutSec", DEFAULT_TIMEOUT))
        if not self.base:
            raise RemoteNotConfigured(
                f"环境变量 {base_env} 未设置 → 本 skill 当前以**纯本地**运行（免费层，功能完整）。"
                f"如需远程增强：设置该变量为你的知识服务地址后重试")
        # 版本协商**启动校验**：远程可用但流程太旧 → 熔断（不得用旧流程读新库）
        v = check_flow_version(root, self.cfg)
        if not v["ok"]:
            raise RemoteVersionTooOld(v["detail"])

    # -- HTTP ---------------------------------------------------------
    def _request(self, path: str, *, body: dict | None = None, headers: dict | None = None):
        url = self.base + path
        data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method="POST" if body is not None else "GET")
        req.add_header("Accept", "application/json")
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        for k, v in (headers or {}).items():
            req.add_header(k, v)
        last = None
        for _ in range(MAX_RETRY + 1):          # 次数**有上限**，不做无限重试
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    return r.status, dict(r.headers), r.read().decode("utf-8")
            except urllib.error.HTTPError as e:
                if e.code == HTTP_PAY_REQUIRED:                     # 402 是**正常业务分支**
                    return e.code, dict(e.headers), e.read().decode("utf-8", "replace")
                last = e
            except (urllib.error.URLError, TimeoutError, OSError) as e:
                last = e
        raise RemoteUnavailable(f"远程知识服务不可达（已重试 {MAX_RETRY} 次）：{last}")

    def _ep(self, name: str) -> str:
        return self.cfg.get("endpoints", {}).get(name, f"/{name}")

    # -- ③ get -------------------------------------------------------
    def get(self, eid: str) -> dict | None:
        return self._get(eid, out_trade_no=None)

    def retry_get(self, eid: str, out_trade_no: str) -> dict | None:
        """支付后重试：带 `X-Out-Trade-No` 再取一次（Body 与首次一致）。

        这是 skill-paid 契约的**服务端侧呼应**——首次 402 拿到 out_trade_no，
        支付完成后凭它重试即可取回正文（服务端查单验证后履约，幂等）。
        """
        return self._get(eid, out_trade_no=out_trade_no)

    def _get(self, eid: str, out_trade_no: str | None) -> dict | None:
        path = self._ep("get").replace("{id}", eid)
        hdrs = {HEADER_OUT_TRADE_NO: out_trade_no} if out_trade_no else None
        status, hdrs_out, text = self._request(path, headers=hdrs)
        if status == HTTP_PAY_REQUIRED:
            code = hdrs_out.get(HEADER_PAY_REQUIRED, "")
            otn = hdrs_out.get(HEADER_OUT_TRADE_NO, "")
            raise PayRequired(code, otn, eid)
        if status == 404:
            return None
        if status != 200:
            raise RemoteUnavailable(f"远程 get({eid}) 返回 HTTP {status}")
        try:
            obj = json.loads(text)
        except ValueError as e:
            raise RemoteUnavailable(f"远程 get({eid}) 返回非 JSON：{e}")
        body = obj.get("body", "")
        # ④ 完整性契约：远程正文必须与其声明 hash 一致，否则拒绝（防"远端悄悄改内容"）
        if obj.get("hash") and obj["hash"] != sha256_of(body):
            raise RemoteIntegrityError(
                f"{eid} 远程正文与声明 hash 不符（可能被篡改 / 缓存脏）→ 拒绝使用")
        return {"id": eid, "kind": obj.get("kind", ""), "block": obj.get("block", ""),
                "title": obj.get("title", ""), "version": obj.get("version", ""),
                "body": body, "hash": obj.get("hash") or sha256_of(body), "source": "remote"}

    # -- ② index -----------------------------------------------------
    def index(self) -> dict:
        status, _, text = self._request(self._ep("index"))
        if status != 200:
            raise RemoteUnavailable(f"远程 index 返回 HTTP {status}")
        return json.loads(text)

    # -- ③ search ----------------------------------------------------
    def search(self, block=None, theme=None, tag=None, text=None, limit=5) -> list[dict]:
        status, _, raw = self._request(self._ep("search"), body={
            "block": block, "theme": theme, "tag": tag, "text": text, "limit": limit})
        if status != 200:
            raise RemoteUnavailable(f"远程 search 返回 HTTP {status}")
        return json.loads(raw).get("hits", [])

    # -- ④ verify ----------------------------------------------------
    def verify(self, strict: bool = False) -> dict:
        status, _, text = self._request(self._ep("verify"))
        if status != 200:
            raise RemoteUnavailable(f"远程 verify 返回 HTTP {status}")
        return json.loads(text)

    # -- 版本协商（ADR §2.4 / §9.7）----------------------------------
    @staticmethod
    def negotiate(local_flow_version: str, remote_manifest: dict) -> dict:
        """流程 ↔ 知识库 版本协商：这是**第四处一致性面**，不预设契约就会复现「双落点漂移」。

        规则：远程 manifest 声明 `minFlowVersion`；本地流程版本低于它 → **熔断 + 升级指引**
        （不容忍"静默用旧流程跑新库"）。
        """
        need = str(remote_manifest.get("minFlowVersion", "")).strip()
        if not need:
            return {"ok": True, "detail": "远程未声明 minFlowVersion（跳过协商）"}
        def key(v: str):
            return tuple(int(x) for x in v.split(".") if x.isdigit())
        if key(local_flow_version) < key(need):
            return {"ok": False,
                    "detail": f"本地流程 {local_flow_version} < 远程库要求的 {need}"
                              f" → 请升级 skill-designer 本体（或加 --backend local 用本地库）"}
        return {"ok": True, "detail": f"流程 {local_flow_version} ≥ 要求 {need}"}


def make_backend(root: Path, mode: str = "local"):
    """后端工厂：`local` / `remote` / `auto`。

    `auto` 语义 = **远程优先 + 本地兜底 + 不静默降级**：
      · 远程未配置    → 直接本地（这是免费层用户的正常路径，不该打扰）
      · 远程可用      → 用远程
      · 远程**故障**  → 回落本地，但**必须打印告警**（不许静默——否则用户永远不知道远程坏了）
      · 本地也没有该条 → 抛熔断错误，给可执行动作（DP-210）
    """
    from knowledge import LocalBackend        # 延迟导入，避免与 knowledge 形成循环
    local = LocalBackend(root)
    if mode == "local":
        return local, None
    try:
        remote = RemoteBackend(root)
    except RemoteNotConfigured as e:
        if mode == "auto":
            return local, None                # 免费层正常路径：静默用本地
        raise RemoteNotConfigured(
            f"{e}\n   替代动作：① 加 `--backend local` 用本地全量（功能不减弱）；"
            f"② 或加 `--backend auto` 让它在远程不可用时自动回落本地") from None
    except RemoteVersionTooOld as e:
        # 版本协商失败：远程在线但**我们读不了**（旧流程读新库会语义错位）。
        # auto 下回落本地是安全的（本地是完整免费层），但**必须出声**——
        # 静默回落会让用户以为在用增强服务，实际一直在用本地（"看起来成功的错误状态"）。
        if mode == "auto":
            print(f"⚠️  远程增强服务暂不可用（版本协商未通过）：{e}\n"
                  f"   已回落本地全量（功能不减弱）。修法：升级 skill-designer 本体。", file=sys.stderr)
            return local, None
        raise RemoteVersionTooOld(
            f"{e}\n   替代动作：① 升级 skill-designer 本体（推荐）；"
            f"② 应急加 `--backend local` 走本地全量；"
            f"③ 或加 `--backend auto` 让它自动回落本地并告警") from None
    if mode == "remote":
        return remote, None
    return remote, local                       # auto


if __name__ == "__main__":
    cfg = {"schemaVersion": "1.0", "模块": "knowledge_remote", "状态": "衔接位（阶段1 预留）"}
    print(json.dumps(cfg, ensure_ascii=False, indent=2))
    print(f"契约常量：{HEADER_PAY_REQUIRED} / {HEADER_OUT_TRADE_NO} / HTTP {HTTP_PAY_REQUIRED}")
