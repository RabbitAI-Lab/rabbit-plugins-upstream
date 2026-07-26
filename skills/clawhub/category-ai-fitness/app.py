"""
类目 AI 改图适配度分析器 - Streamlit Web UI

启动:
    cd ~/.openclaw/workspace/skills/category-ai-fitness
    streamlit run app.py
"""
from __future__ import annotations

import datetime
import io
import json
import os
import platform
import subprocess
import sys
from pathlib import Path

import requests as _requests

import pandas as pd
import streamlit as st

ROOT = Path(__file__).parent
SCRIPTS_DIR = ROOT / "scripts"
OUTPUT_DIR = ROOT / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(SCRIPTS_DIR))


def _load_openclaw_env():
    cfg_path = Path.home() / ".openclaw" / "openclaw.json"
    if not cfg_path.exists():
        return
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        env_dict = cfg.get("env", {}) or {}
        for k, v in env_dict.items():
            if isinstance(v, str) and k not in os.environ:
                os.environ[k] = v
        for k, v in cfg.items():
            if isinstance(v, str) and k.isupper() and k not in os.environ:
                os.environ[k] = v
    except Exception:
        pass


_load_openclaw_env()

FEISHU_WEBHOOK = os.environ.get("FEISHU_WEBHOOK_CATEGORY_FITNESS", "https://open.feishu.cn/open-apis/bot/v2/hook/d85979a8-55d6-45f0-a6cb-a1654a2ce948")


def push_feishu(results: list, report_path: str):
    """分析完成后推送汇总到飞书群"""
    counts = {"AI改图搬": 0, "可改图搬": 0, "白底直搬": 0, "谨慎": 0, "弃": 0}
    for r in results:
        d = str(r.get("decision", ""))
        if "AI改图搬" in d:
            counts["AI改图搬"] += 1
        elif "可改图搬" in d:
            counts["可改图搬"] += 1
        elif "白底直搬" in d:
            counts["白底直搬"] += 1
        elif "⚠️" in d:
            counts["谨慎"] += 1
        elif "❌" in d:
            counts["弃"] += 1

    top_items = []
    for r in results:
        d = str(r.get("decision", ""))
        if "✅" in d:
            top_items.append(f"  • {r.get('keyword', '')} → {d}")
    top_text = "\n".join(top_items[:10]) if top_items else "  （无推荐类目）"

    content = (
        f"📊 **类目选品完成**\n\n"
        f"共 {len(results)} 个类目：\n"
        f"  ✅ AI改图搬: {counts['AI改图搬']}\n"
        f"  ✅ 可改图搬: {counts['可改图搬']}\n"
        f"  ✅ 白底直搬: {counts['白底直搬']}\n"
        f"  ⚠️ 谨慎: {counts['谨慎']}\n"
        f"  ❌ 弃: {counts['弃']}\n\n"
        f"**推荐类目：**\n{top_text}\n\n"
        f"报告: {Path(report_path).name}"
    )

    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": "类目选品分析报告"},
                "template": "green",
            },
            "elements": [{"tag": "markdown", "content": content}],
        },
    }
    try:
        _requests.post(FEISHU_WEBHOOK, json=payload, timeout=10)
    except Exception:
        pass


from category_parser import detect_platform, load_categories  # noqa: E402
from amazon_fetcher import enrich_with_images, fetch_amazon_top_products  # noqa: E402
from walmart_fetcher import fetch_walmart_top_products  # noqa: E402
from vision_analyzer import CACHE_DIR as IMG_CACHE_DIR  # noqa: E402
from vision_analyzer import analyze_images_batch, download_image  # noqa: E402
from scorer import score_category  # noqa: E402
from excel_writer import write_excel  # noqa: E402


st.set_page_config(
    page_title="类目 AI 改图适配度分析器",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 16px;
    border-radius: 12px;
    color: white;
    margin: 8px 0;
}
.metric-card-green { background: linear-gradient(135deg, #11998e, #38ef7d); }
.metric-card-blue  { background: linear-gradient(135deg, #4facfe, #00f2fe); }
.metric-card-orange { background: linear-gradient(135deg, #f7971e, #ffd200); }
.metric-card-red    { background: linear-gradient(135deg, #cb2d3e, #ef473a); }
.report-link {
    color: #4338ca;
    text-decoration: none;
    font-weight: 500;
}
.report-link:hover { text-decoration: underline; }
</style>
""", unsafe_allow_html=True)


def open_local_file(path: str):
    """跨平台打开本地文件（Mac/Windows/Linux）"""
    p = Path(path).resolve()
    if not p.exists():
        return False
    try:
        if platform.system() == "Darwin":
            subprocess.Popen(["open", str(p)])
        elif platform.system() == "Windows":
            os.startfile(str(p))
        else:
            subprocess.Popen(["xdg-open", str(p)])
        return True
    except Exception:
        return False


def show_in_finder(path: str):
    """在 Finder/资源管理器中显示文件"""
    p = Path(path).resolve()
    if not p.exists():
        return False
    try:
        if platform.system() == "Darwin":
            subprocess.Popen(["open", "-R", str(p)])
        elif platform.system() == "Windows":
            subprocess.Popen(["explorer", "/select,", str(p)])
        else:
            subprocess.Popen(["xdg-open", str(p.parent)])
        return True
    except Exception:
        return False


def parse_text_input(text: str) -> list:
    """从 textarea 输入解析类目列表"""
    cats = []
    for idx, line in enumerate(text.splitlines()):
        line = line.strip()
        if not line:
            continue
        parsed = detect_platform(line)
        if parsed:
            parsed["row_index"] = idx
            cats.append(parsed)
    return cats


def analyze_one_category(cat: dict, top_n: int, amazon_only: bool, walmart_only: bool, status_callback=None) -> dict:
    """对单个类目跑全流程，并通过回调通知进度"""
    keyword = cat["search_keyword"]
    platform_name = cat["platform"]
    products = []

    if not walmart_only and platform_name in ("amazon", "both"):
        if status_callback:
            status_callback(f"🔍 [Amazon] 抓取「{keyword}」...")
        try:
            amz_products = fetch_amazon_top_products(keyword, top_n=top_n)
            if status_callback:
                status_callback(f"🖼️  [Amazon] 补全 {len(amz_products)} 张主图...")
            amz_products = enrich_with_images(amz_products)
            products.extend(amz_products)
        except Exception as e:
            if status_callback:
                status_callback(f"⚠️  [Amazon] 抓取失败: {e}")

    if not amazon_only and platform_name in ("walmart", "both"):
        if status_callback:
            status_callback(f"🔍 [Walmart] 抓取「{keyword}」...")
        try:
            wm_products = fetch_walmart_top_products(keyword, top_n=top_n)
            products.extend(wm_products)
        except Exception as e:
            if status_callback:
                status_callback(f"⚠️  [Walmart] 抓取失败: {e}")

    if not products:
        return {**_base_row(cat), **_empty_score()}

    image_urls = [p.get("image", "") for p in products if p.get("image")]
    if status_callback:
        status_callback(f"🤖 [Claude] 分析 {len(image_urls)} 张主图...")

    vision_results = analyze_images_batch(image_urls, max_workers=5)
    score = score_category(products, vision_results)

    rep_images = []
    raw_samples = []
    for p, v in zip(products, vision_results):
        if v and "error" not in v:
            raw_samples.append({"product": p, "vision": v})
            if p.get("image") and len(rep_images) < 3:
                rep_images.append(p["image"])

    return {
        **_base_row(cat),
        **score,
        "representative_images": rep_images,
        "raw_samples": raw_samples,
    }


def _base_row(cat: dict) -> dict:
    return {
        "raw_input": cat["raw"],
        "platform": cat["platform"],
        "keyword": cat["search_keyword"],
        "fetched_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


def _empty_score() -> dict:
    return {
        "scene_fitness": 0,
        "ai_difficulty": "无数据",
        "infringement_risk": "无数据",
        "must_modify_image": False,
        "strategy": "无数据",
        "decision": "❌无数据",
        "reason": "未抓到任何商品",
        "dominant_form": "unknown",
        "lifestyle_ratio": 0,
        "white_ratio": 0,
        "median_price": None,
        "median_sales": None,
        "sample_count": 0,
        "representative_images": [],
    }


def render_summary_cards(rows: list):
    """汇总统计卡片"""
    if not rows:
        return
    counts = {"✅AI改图搬": 0, "✅白底直搬": 0, "✅可改图搬": 0, "⚠️": 0, "❌": 0}
    for r in rows:
        d = str(r.get("decision", ""))
        if "✅AI改图搬" in d:
            counts["✅AI改图搬"] += 1
        elif "✅白底直搬" in d:
            counts["✅白底直搬"] += 1
        elif "✅可改图搬" in d:
            counts["✅可改图搬"] += 1
        elif "⚠️" in d:
            counts["⚠️"] += 1
        elif "❌" in d:
            counts["❌"] += 1

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("✅ AI改图搬", counts["✅AI改图搬"])
    c2.metric("✅ 可改图搬", counts["✅可改图搬"])
    c3.metric("✅ 白底直搬", counts["✅白底直搬"])
    c4.metric("⚠️ 谨慎", counts["⚠️"])
    c5.metric("❌ 弃", counts["❌"])


def render_results_table(rows: list):
    """结果表格（含决策颜色高亮 + 缩略图）"""
    if not rows:
        return
    df = pd.DataFrame([{
        "类目": r.get("raw_input", ""),
        "平台": r.get("platform", ""),
        "关键词": r.get("keyword", ""),
        "样本": r.get("sample_count", 0),
        "📊 场景化适配": r.get("scene_fitness", 0),
        "AI难度": r.get("ai_difficulty", ""),
        "改图策略": r.get("strategy", ""),
        "🎨 侵权风险": r.get("infringement_risk", ""),
        "图片同质化": r.get("uniqueness_risk", ""),
        "必须改图": "✅" if r.get("must_modify_image") else "",
        "场景图%": f"{r.get('lifestyle_ratio', 0)*100:.0f}%",
        "白底%": f"{r.get('white_ratio', 0)*100:.0f}%",
        "主导形态": r.get("dominant_form", ""),
        "中位价": f"${r.get('median_price'):.2f}" if r.get("median_price") else "—",
        "中位月销": str(r.get("median_sales")) if r.get("median_sales") else "—",
        "⭐ 决策": r.get("decision", ""),
        "决策理由": r.get("reason", ""),
        "⚠️ IP风险预警": r.get("ip_warning", ""),
    } for r in rows])

    def highlight_decision(val):
        s = str(val)
        if "✅AI改图搬" in s:
            return "background-color: #c6efce; font-weight: bold"
        if "✅可改图搬" in s:
            return "background-color: #d4edda; font-weight: bold"
        if "✅白底直搬" in s:
            return "background-color: #dce6f1; font-weight: bold"
        if "⚠️" in s:
            return "background-color: #ffeb9c; font-weight: bold"
        if "❌" in s:
            return "background-color: #ffc7ce; font-weight: bold"
        return ""

    def highlight_risk(val):
        s = str(val)
        if "🔴" in s:
            return "background-color: #ffc7ce"
        if "🟡" in s:
            return "background-color: #ffeb9c"
        if "🟢" in s:
            return "background-color: #c6efce"
        return ""

    styled = df.style.map(highlight_decision, subset=["⭐ 决策"]).map(highlight_risk, subset=["🎨 侵权风险", "图片同质化"])
    st.dataframe(styled, width="stretch", height=min(600, 60 + len(rows) * 38))


def render_image_gallery(rows: list):
    """每个类目的代表图缩略图展示"""
    if not rows:
        return
    with st.expander("🖼️  查看每类目代表主图", expanded=False):
        for r in rows:
            st.markdown(f"**{r.get('raw_input', '')}** — {r.get('decision', '')}")
            imgs = r.get("representative_images", [])
            if imgs:
                cols = st.columns(min(len(imgs), 3))
                for i, url in enumerate(imgs[:3]):
                    with cols[i]:
                        try:
                            st.image(url, width=180)
                        except Exception:
                            st.text("(图片加载失败)")
            else:
                st.caption("无图片")
            st.divider()


def list_history_reports() -> list:
    """列出 output/ 目录下的历史报告"""
    files = sorted(OUTPUT_DIR.glob("category_fitness_report_*.xlsx"), key=lambda p: p.stat().st_mtime, reverse=True)
    return files[:20]


def main():
    st.title("📊 类目 AI 改图适配度分析器")
    st.caption("输入三级类目 → 自动抓取 Amazon TOP 商品主图 → Claude 多模态分析 → 输出决策报告")

    if "results" not in st.session_state:
        st.session_state.results = []
    if "running" not in st.session_state:
        st.session_state.running = False
    if "last_report_path" not in st.session_state:
        st.session_state.last_report_path = None

    with st.sidebar:
        st.header("📥 输入类目")

        input_mode = st.radio(
            "输入方式",
            ["📝 手动输入", "📂 上传 Excel/CSV"],
            horizontal=True,
        )

        categories = []

        if input_mode == "📝 手动输入":
            text = st.text_area(
                "类目（每行一个）",
                placeholder="支持以下格式：\n- 关键词：outdoor furniture\n- 路径：Home & Kitchen > Bedding > Sheets\n- Amazon URL\n- Walmart URL",
                height=200,
            )
            if text.strip():
                categories = parse_text_input(text)
                st.success(f"✓ 解析到 {len(categories)} 个类目")
        else:
            uploaded = st.file_uploader("选择 Excel/CSV 文件", type=["xlsx", "xls", "csv"])
            if uploaded:
                tmp_path = OUTPUT_DIR / f"_uploaded_{uploaded.name}"
                tmp_path.write_bytes(uploaded.getbuffer())
                try:
                    categories = load_categories(str(tmp_path))
                    st.success(f"✓ 解析到 {len(categories)} 个类目")
                except Exception as e:
                    st.error(f"解析失败: {e}")

        st.divider()
        st.header("⚙️ 参数")
        top_n = st.slider("每类目抓取数量", 10, 60, 50)
        amazon_only = st.checkbox("仅 Amazon（推荐）", value=True, help="Walmart 反爬严，默认关闭")

        st.divider()
        start_btn = st.button(
            "🚀 开始分析",
            type="primary",
            use_container_width=True,
            disabled=(not categories or st.session_state.running),
        )

        if categories and not st.session_state.running:
            with st.expander(f"📋 待分析 {len(categories)} 个类目", expanded=False):
                for c in categories[:10]:
                    st.text(f"• [{c['platform']}] {c['search_keyword']}")
                if len(categories) > 10:
                    st.caption(f"... 还有 {len(categories) - 10} 个")

        st.divider()
        st.header("📁 历史报告")
        history = list_history_reports()
        if history:
            for f in history[:10]:
                col1, col2 = st.columns([3, 1])
                with col1:
                    label = f"📄 {f.name.replace('category_fitness_report_', '').replace('.xlsx', '')}"
                    if st.button(label, key=f"open_{f.name}", use_container_width=True):
                        if open_local_file(str(f)):
                            st.toast(f"✓ 已打开: {f.name}")
                        else:
                            st.error("打开失败")
                with col2:
                    if st.button("📂", key=f"finder_{f.name}", help="在 Finder 中显示"):
                        show_in_finder(str(f))
        else:
            st.caption("（暂无历史报告）")

    if start_btn and categories:
        st.session_state.running = True
        st.session_state.results = []
        st.rerun()

    if st.session_state.running:
        st.subheader("⏳ 分析进行中")
        progress_bar = st.progress(0.0)
        status_box = st.empty()
        results_placeholder = st.container()

        for i, cat in enumerate(categories):
            progress_bar.progress((i) / len(categories), text=f"[{i + 1}/{len(categories)}] {cat['search_keyword']}")

            def status_cb(msg, _i=i, _kw=cat["search_keyword"]):
                status_box.info(f"[{_i + 1}/{len(categories)}] {msg}")

            row = analyze_one_category(cat, top_n, amazon_only, False, status_callback=status_cb)
            st.session_state.results.append(row)

            with results_placeholder:
                st.empty()
                render_summary_cards(st.session_state.results)
                render_results_table(st.session_state.results)

        progress_bar.progress(1.0, text="✅ 全部完成")
        status_box.success(f"✓ 分析完成，共 {len(st.session_state.results)} 个类目")

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = OUTPUT_DIR / f"category_fitness_report_{ts}.xlsx"
        write_excel(st.session_state.results, str(out_path), IMG_CACHE_DIR)
        push_feishu(st.session_state.results, str(out_path))
        st.session_state.last_report_path = str(out_path)
        st.session_state.running = False
        st.rerun()

    if st.session_state.results and not st.session_state.running:
        st.subheader("📈 汇总")
        render_summary_cards(st.session_state.results)

        st.subheader("📋 详细结果")
        render_results_table(st.session_state.results)

        render_image_gallery(st.session_state.results)

        if st.session_state.last_report_path:
            st.divider()
            st.subheader("📥 下载报告")
            report_path = st.session_state.last_report_path

            c1, c2, c3 = st.columns(3)

            with c1:
                if Path(report_path).exists():
                    with open(report_path, "rb") as f:
                        st.download_button(
                            "⬇️  下载 Excel",
                            data=f.read(),
                            file_name=Path(report_path).name,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                            use_container_width=True,
                        )

            with c2:
                if st.button("📂  打开本地 Excel", use_container_width=True):
                    if open_local_file(report_path):
                        st.toast(f"✓ 已用默认应用打开")
                    else:
                        st.error("打开失败")

            with c3:
                if st.button("🔍  在 Finder 中显示", use_container_width=True):
                    show_in_finder(report_path)

            st.code(report_path, language=None)

    if not st.session_state.results and not st.session_state.running:
        st.info("👈 在左侧侧边栏输入类目或上传文件，然后点击「开始分析」")
        st.markdown("""
        ### 使用说明

        1. **输入类目**（侧边栏）
           - 手动输入：每行一个，支持关键词、类目路径、URL
           - 上传文件：Excel/CSV，自动识别类目列

        2. **设置参数**
           - 每类目抓取数量：默认 10（5-20 可调）
           - 仅 Amazon：默认开启（Walmart 反爬严重）

        3. **开始分析**
           - 实时显示每个类目的抓取/分析进度
           - 完成的类目实时追加到结果表格
           - 决策档位用颜色高亮（绿/蓝/黄/红）

        4. **下载/打开报告**
           - Excel 自动保存到 `output/` 目录
           - 历史报告在侧边栏可一键打开
           - 点击「📂 打开本地 Excel」直接用 Excel 打开

        ### 决策档位说明

        | 档位 | 含义 |
        |------|------|
        | ✅ AI改图搬 | 类目适合场景化，AI 改图优先 |
        | ✅ 白底直搬 | 替换件/工具类，白底图搜索权重高 |
        | ⚠️ 谨慎 | 需要人工评估或 AI 改图难度高 |
        | ❌ 弃 | 不建议搬运 |
        """)


if __name__ == "__main__":
    main()
