#!/usr/bin/env python3
"""销售数据分析技能：独立 CLI 脚本，供 OpenClaw 通过 bash exec 调用，输出 JSON。
支持: query 查询 / plot 图表 / trend 趋势 / report 导出 PDF 报告
"""

import os
import sys
import json
from datetime import datetime

import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "sales.csv")
CHART_DIR = "/tmp"
FONT_PATH = os.path.join(BASE_DIR, "fonts", "wqy-microhei.ttc")
REPORT_DIR = os.path.join(BASE_DIR, "reports")


def _df():
    if not os.path.exists(CSV_PATH):
        sys.exit(json.dumps({"error": "sales.csv 不存在"}, ensure_ascii=False))
    return pd.read_csv(CSV_PATH)


def query(question: str) -> str:
    df = _df()
    q = question.lower()
    if "最高" in q or "最大" in q:
        if "利润" in q:
            row = df.loc[df["profit"].idxmax()]
            return f"利润最高的记录是{row['month']}月{row['region']}地区{row['product']}产品，利润为{row['profit']}"
        if "数量" in q or "销量" in q:
            row = df.loc[df["quantity"].idxmax()]
            return f"销量最高的记录是{row['month']}月{row['region']}地区{row['product']}产品，销量为{row['quantity']}"
        row = df.loc[df["sales"].idxmax()]
        return f"销售额最高的记录是{row['month']}月{row['region']}地区{row['product']}产品，销售额为{row['sales']}"
    if "总销售额" in q:
        return f"总销售额为{df['sales'].sum()}"
    if "总利润" in q:
        return f"总利润为{df['profit'].sum()}"
    if "总销量" in q or "总数量" in q:
        return f"总销量为{df['quantity'].sum()}"
    if "月" in q and ("汇总" in q or "统计" in q):
        return "按月汇总:\n" + df.groupby("month")[["sales", "profit", "quantity"]].sum().to_string()
    return f"无法理解:{question}"


def plot(chart_type: str = "line", metric: str = "sales") -> str:
    df = _df()
    if chart_type not in ("line", "bar") or metric not in ("sales", "profit", "quantity"):
        return f"不支持的图表类型或指标:{chart_type}/{metric}"
    plt.figure(figsize=(10, 6))
    if chart_type == "line":
        series = df.groupby("month")[metric].sum()
        series.plot(kind="line", marker="o")
        plt.title(f"Monthly {metric.capitalize()} Trend")
    else:
        series = df.groupby("region")[metric].sum()
        series.plot(kind="bar")
        plt.title(f"{metric.capitalize()} by Region")
    img = os.path.join(CHART_DIR, f"sales_{metric}_{chart_type}.png")
    plt.tight_layout()
    plt.savefig(img)
    plt.close()
    return img


def trend(question: str) -> str:
    df = _df()
    q = question.lower()
    if "利润" in q:
        monthly = df.groupby("month")["profit"].sum()
        parts = ["利润变化趋势(按月):"]
        months = list(monthly.index)
        for i in range(1, len(months)):
            diff = monthly.iloc[i] - monthly.iloc[i - 1]
            parts.append(f"{months[i]}月相比{months[i-1]}月:{diff:+}")
        return "\n".join(parts)
    if "销售" in q or "销量" in q:
        monthly = df.groupby("month")["sales"].sum()
        parts = ["销售额变化趋势(按月):"]
        months = list(monthly.index)
        for i in range(1, len(months)):
            diff = monthly.iloc[i] - monthly.iloc[i - 1]
            parts.append(f"{months[i]}月相比{months[i-1]}月:{diff:+}")
        return "\n".join(parts)
    return "请提供更具体的分析问题。"


def _zh_font(size: float = 12):
    """返回中文字体（技能自带 wqy-microhei，避免系统无中文字体导致乱码）。"""
    if os.path.exists(FONT_PATH):
        return FontProperties(fname=FONT_PATH, size=size)
    return FontProperties(size=size)


def parse_report_args(args):
    """解析 report 参数：位置参数=查询问题，--trend=趋势问题，--chart 类型 指标=图表（可多个）。"""
    questions, trends, charts = [], [], []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--trend":
            i += 1
            if i < len(args):
                trends.append(args[i])
        elif a == "--chart":
            i += 1
            if i + 1 < len(args):
                charts.append((args[i], args[i + 1]))
                i += 1
        else:
            questions.append(a)
        i += 1
    if not questions and not trends and not charts:
        questions = ["总销售额", "总利润"]
    return questions, trends, charts


def export_report(questions, trends, charts) -> str:
    """将查询结果与图表整合为 PDF 报告，返回文件路径。"""
    from matplotlib.backends.backend_pdf import PdfPages

    os.makedirs(REPORT_DIR, exist_ok=True)

    # 1) 文字结果
    lines = []
    for q in questions:
        lines.append(("Q: " + q, query(q)))
    for t in trends:
        lines.append(("Q: " + t, trend(t)))

    # 2) 图表（复用 plot 生成 PNG）
    chart_paths = [plot(ct, m) for ct, m in charts if ct in ("line", "bar") and m in ("sales", "profit", "quantity")]

    # 3) 生成 PDF
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = os.path.join(REPORT_DIR, f"sales_report_{ts}.pdf")

    with PdfPages(pdf_path) as pdf:
        # 文字页（A4 竖版）
        fig = plt.figure(figsize=(8.27, 11.69))
        fig.text(0.5, 0.95, "销售数据分析报告", fontproperties=_zh_font(22), ha="center")
        fig.text(0.5, 0.91, f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                 fontproperties=_zh_font(10), ha="center", color="0.45")
        y = 0.86
        for q, r in lines:
            fig.text(0.06, y, q, fontproperties=_zh_font(13), color="#1f4e79")
            y -= 0.04
            for line in str(r).split("\n"):
                fig.text(0.08, y, line, fontproperties=_zh_font(11), wrap=True)
                y -= 0.032
            y -= 0.025
        pdf.savefig(fig)
        plt.close(fig)

        # 图表页（每张图一页）
        for p in chart_paths:
            fig = plt.figure(figsize=(8.27, 11.69))
            ax = fig.add_axes([0.03, 0.05, 0.94, 0.9])
            ax.imshow(plt.imread(p))
            ax.axis("off")
            pdf.savefig(fig)
            plt.close(fig)

    return pdf_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "缺少命令参数"}, ensure_ascii=False))
        sys.exit(1)
    cmd = sys.argv[1]
    try:
        if cmd == "query":
            result = query(" ".join(sys.argv[2:]) or "总销售额")
        elif cmd == "plot":
            ct = sys.argv[2] if len(sys.argv) > 2 else "line"
            m = sys.argv[3] if len(sys.argv) > 3 else "sales"
            p = plot(ct, m)
            result = p if not p.startswith("/") else f"图表已保存为{p}"
        elif cmd == "trend":
            result = trend(" ".join(sys.argv[2:]) or "利润")
        elif cmd == "report":
            questions, trends, charts = parse_report_args(sys.argv[2:])
            result = export_report(questions, trends, charts)
        else:
            result = f"未知命令:{cmd}（支持 query/plot/trend/report）"
        print(json.dumps({"result": result}, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))
        sys.exit(1)
