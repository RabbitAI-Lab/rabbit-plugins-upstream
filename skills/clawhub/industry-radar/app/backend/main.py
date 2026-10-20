"""
智汇简报 IndustryRadar — FastAPI 应用入口。

本地运行：
    cd project/backend
    python3 -m uvicorn main:app --host 0.0.0.0 --port 8000

同时托管前端静态页（project/frontend），因此浏览器直接访问 http://localhost:8000 即可。

云端对应关系（见《方案设计.md》）：
    FastAPI 路由  <->  APIG + FunctionGraph
    store.py      <->  RDS MySQL
    BRIEF_DIR     <->  OBS 对象
"""
from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import Body, FastAPI, Header, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import generator
import store
from config import BASE_DIR, DEMO_PASS, DEMO_USER, USE_LLM
from sources import all_source_meta

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
log = logging.getLogger("industryradar")

app = FastAPI(title="智汇简报 IndustryRadar", version="1.0.0")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"],
)

# 演示用极简会话（生产应换成 JWT + Redis，见方案设计「安全」小节）
_SESSIONS: Dict[str, Dict[str, Any]] = {}


# ------------------------------------------------------------------ 认证
def _hash(pw: str) -> str:
    return hashlib.sha256(("ir_salt_" + pw).encode("utf-8")).hexdigest()


def _token_for(user: Dict) -> str:
    tok = hashlib.sha1(f"{user['id']}-{user['username']}-{time.time()}".encode()).hexdigest()
    _SESSIONS[tok] = {"user_id": user["id"], "username": user["username"], "ts": time.time()}
    return tok


def current_user(authorization: Optional[str]) -> Dict[str, Any]:
    if not authorization:
        raise HTTPException(401, "未登录")
    tok = authorization.replace("Bearer ", "").strip()
    sess = _SESSIONS.get(tok)
    if not sess:
        raise HTTPException(401, "登录已失效，请重新登录")
    return sess


def _own_subscription(sub_id: int, me: Dict[str, Any]) -> Dict[str, Any]:
    """取订阅并校验归属。

    不存在与「不属于当前用户」都返回 404：不泄露资源是否存在，
    也避免调用方通过状态码枚举他人订阅。
    """
    sub = store.get_subscription(sub_id)
    if not sub or sub.get("user_id") != me["user_id"]:
        raise HTTPException(404, "订阅不存在")
    return sub


def _own_briefing(briefing_id: int, me: Dict[str, Any]) -> Dict[str, Any]:
    """取简报并顺着 subscription_id 校验归属；同样用 404 统一口径。"""
    b = store.get_briefing(briefing_id)
    if not b:
        raise HTTPException(404, "简报不存在")
    sub = store.get_subscription(b["subscription_id"])
    if not sub or sub.get("user_id") != me["user_id"]:
        raise HTTPException(404, "简报不存在")
    return b


def _own_subscription(sub_id: int, me: Dict[str, Any]) -> Dict[str, Any]:
    """取订阅并校验归属。

    不存在与「不属于当前用户」都返回 404：不泄露资源是否存在，
    也避免调用方通过状态码枚举他人订阅。
    """
    sub = store.get_subscription(sub_id)
    if not sub or sub.get("user_id") != me["user_id"]:
        raise HTTPException(404, "订阅不存在")
    return sub


def _own_briefing(briefing_id: int, me: Dict[str, Any]) -> Dict[str, Any]:
    """取简报并顺着 subscription_id 校验归属；同样用 404 统一口径。"""
    b = store.get_briefing(briefing_id)
    if not b:
        raise HTTPException(404, "简报不存在")
    sub = store.get_subscription(b["subscription_id"])
    if not sub or sub.get("user_id") != me["user_id"]:
        raise HTTPException(404, "简报不存在")
    return b


def _ensure_demo_user() -> Dict[str, Any]:
    u = store.get_user_by_name(DEMO_USER)
    if not u:
        uid = store.create_user(DEMO_USER, _hash(DEMO_PASS), "demo@example.com")
        u = store.get_user_by_name(DEMO_USER)
        # 预置一个示例订阅，首次进入即可看到效果
        store.create_subscription(
            uid, "新能源汽车 × 固态电池", "新能源汽车,汽车", "固态电池,电池,续航",
            "量产,车企", json.dumps(["36kr", "zhihu_daily", "techcrunch"]),
        )
    return u


@app.on_event("startup")
def _startup() -> None:
    store.init_db()
    _ensure_demo_user()
    log.info("IndustryRadar started. LLM=%s", "on" if USE_LLM else "off(fallback)")


# ------------------------------------------------------------------ 模型
class LoginIn(BaseModel):
    username: str
    password: str


class SubIn(BaseModel):
    name: str
    industry_kw: str
    tech_kw: str
    extra_kw: str = ""
    sources: List[str] = []
    frequency: str = "weekly"
    style: str = "standard"      # standard 标准周报 / curated 编辑精选


class SubPatch(BaseModel):
    name: Optional[str] = None
    industry_kw: Optional[str] = None
    tech_kw: Optional[str] = None
    extra_kw: Optional[str] = None
    sources: Optional[List[str]] = None
    frequency: Optional[str] = None
    style: Optional[str] = None
    enabled: Optional[int] = None


class PreviewIn(BaseModel):
    industry_kw: str
    tech_kw: str
    extra_kw: str = ""
    sources: List[str] = []


# ------------------------------------------------------------------ API
@app.post("/api/login")
def login(body: LoginIn) -> Dict[str, Any]:
    u = store.get_user_by_name(body.username)
    if not u or u["password_hash"] != _hash(body.password):
        raise HTTPException(401, "用户名或密码错误")
    return {"token": _token_for(u), "username": u["username"], "user_id": u["id"]}


@app.get("/api/sources")
def list_sources() -> Dict[str, Any]:
    return {"sources": all_source_meta()}


@app.get("/api/config")
def get_config() -> Dict[str, Any]:
    """前端展示当前运行模式（LLM 在线 / 离线降级）。"""
    return {
        "llm_enabled": USE_LLM,
        "mode": "在线大模型" if USE_LLM else "离线规则引擎（可配置 LLM）",
        "version": app.version,
    }


@app.get("/api/subscriptions")
def get_subscriptions(authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    return {"subscriptions": store.list_subscriptions(me["user_id"])}


@app.post("/api/subscriptions")
def post_subscription(body: SubIn, authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    if not body.name or not body.industry_kw or not body.tech_kw:
        raise HTTPException(400, "名称 / 行业词 / 技术词 均为必填")
    sid = store.create_subscription(
        me["user_id"], body.name, body.industry_kw, body.tech_kw,
        body.extra_kw, json.dumps(body.sources, ensure_ascii=False), body.frequency,
        style=(body.style or "standard"),
    )
    return {"id": sid, "message": "创建成功"}


@app.put("/api/subscriptions/{sub_id}")
def put_subscription(sub_id: int, body: SubPatch,
                     authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    _own_subscription(sub_id, me)
    fields = body.model_dump(exclude_none=True)
    if "sources" in fields:
        fields["sources_json"] = json.dumps(fields.pop("sources"), ensure_ascii=False)
    store.update_subscription(sub_id, fields)
    return {"message": "更新成功"}


@app.delete("/api/subscriptions/{sub_id}")
def del_subscription(sub_id: int, authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    _own_subscription(sub_id, me)
    store.delete_subscription(sub_id)
    return {"message": "已删除"}


@app.post("/api/subscriptions/{sub_id}/run")
def run_subscription(sub_id: int, authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    """手动触发一次简报生成（等价于云端 TIMER 触发）。"""
    me = current_user(authorization)
    sub = _own_subscription(sub_id, me)
    try:
        result = generator.run_pipeline(sub, save=True)
    except Exception as exc:  # noqa: BLE001
        log.exception("pipeline failed")
        raise HTTPException(500, f"生成失败：{exc}") from exc
    return {
        "briefing_id": result["briefing_id"],
        "title": result["title"],
        "stats": result["stats"],
        "message": "简报生成完成",
    }


@app.post("/api/preview")
def preview(body: PreviewIn, authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    """关键词预览：跑一遍 pipeline 但不落库，方便控制台即时看效果。"""
    current_user(authorization)
    sub = {
        "id": 0,
        "name": f"{body.industry_kw} × {body.tech_kw}",
        "industry_kw": body.industry_kw,
        "tech_kw": body.tech_kw,
        "extra_kw": body.extra_kw,
        "sources_json": json.dumps(body.sources, ensure_ascii=False),
        "user_id": 0,
    }
    result = generator.run_pipeline(sub, save=False)
    return {"markdown": result["markdown"], "stats": result["stats"]}


@app.get("/api/articles")
def get_articles(subscription_id: int = Query(...), limit: int = 100,
                 authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    _own_subscription(subscription_id, me)
    return {"articles": store.list_articles(subscription_id, limit)}


@app.get("/api/briefings")
def get_briefings(subscription_id: int = Query(...),
                  authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    _own_subscription(subscription_id, me)
    items = store.list_briefings(subscription_id)
    for b in items:
        b.pop("md_path", None)
    return {"briefings": items}


@app.get("/api/briefings/{briefing_id}")
def get_briefing(briefing_id: int, authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    b = _own_briefing(briefing_id, me)
    b["markdown"] = _read_md(b.get("md_path", ""))
    return b


@app.get("/api/briefings/{briefing_id}/export", response_class=PlainTextResponse)
def export_briefing(briefing_id: int, fmt: str = "md",
                    authorization: Optional[str] = Header(None)) -> PlainTextResponse:
    me = current_user(authorization)
    b = _own_briefing(briefing_id, me)
    md = _read_md(b.get("md_path", ""))
    filename = f"briefing_{briefing_id}.md"
    return PlainTextResponse(
        md, media_type="text/markdown; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.get("/api/trend")
def get_trend(subscription_id: int = Query(...),
              authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    me = current_user(authorization)
    _own_subscription(subscription_id, me)
    return store.trend_data(subscription_id)


@app.get("/api/dashboard")
def dashboard(authorization: Optional[str] = Header(None)) -> Dict[str, Any]:
    """控制台总览：订阅数 / 简报数 / 文章数。"""
    me = current_user(authorization)
    subs = store.list_subscriptions(me["user_id"])
    briefings = sum(s.get("briefing_count", 0) for s in subs)
    articles = 0
    for s in subs:
        articles += len(store.list_articles(s["id"], limit=1000))
    return {
        "subscription_count": len(subs),
        "briefing_count": briefings,
        "article_count": articles,
        "llm_enabled": USE_LLM,
    }


def _read_md(path: str) -> str:
    try:
        p = Path(path)
        if p.exists():
            return p.read_text(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    return ""


# ------------------------------------------------------------ 静态前端托管
_FRONTEND = BASE_DIR / "frontend"
if _FRONTEND.exists():
    app.mount("/", StaticFiles(directory=str(_FRONTEND), html=True), name="frontend")