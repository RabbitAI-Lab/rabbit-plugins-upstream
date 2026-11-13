#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
agent_gov_toolkit.py — AI 智能体治理本地工具包
仅使用 Python 标准库，零网络、零数据采集。

命令：
  risk       --agent "<Agent描述>"   Agent 风险清单与等级
  perm       --tools "..." --required "..."   权限评估（最小权限检查）
  maturity   --scores "a,b,c,d,e,f"   治理成熟度自评（6 维度 1-5 分）
  liability  --scene "<事故场景>"     责任分配建议
  regulation --region <cn|sg|intl>    监管要点速查
  --help                             查看帮助
"""

import argparse
import sys

VERSION = "1.0.0"

# ---------------------------------------------------------------- risk

RISK_KEYWORDS = {
    "perm_scope": {
        5: ["写", "修改", "删除", "下单", "转账", "发邮件", "数据库", "生产", "机密", "支付"],
        3: ["读", "查询", "内部", "CRM", "系统"],
        1: ["只读", "公开", "沙箱"],
    },
    "autonomy": {
        5: ["自主", "全自主", "无人", "自动执行", "定时", "批量"],
        3: ["半自动", "条件", "部分"],
        1: ["人工确认", "每步", "人审", "建议"],
    },
    "impact": {
        5: ["订单", "转账", "付款", "删除", "敏感", "个人", "对外", "合同"],
        3: ["内部", "记录", "邮件"],
        1: ["可回滚", "草稿", "查询"],
    },
    "exposure": {
        5: ["对外", "公开", "客户", "互联网", "公网"],
        3: ["内部", "员工"],
        1: ["本地", "个人"],
    },
}

HIGH_RISK_TRIGGER = ["订单", "转账", "付款", "删除", "机密", "自主"]


def _score(text, bank):
    best = 1
    for s in (5, 3, 1):
        for kw in bank.get(s, []):
            if kw in text:
                best = max(best, s)
    return best


def risk(agent):
    if not agent or not agent.strip():
        print("错误：--agent 不能为空。示例：--agent \"客户服务Agent，可访问CRM、可发邮件、可下订单\"")
        return 2
    weights = {"perm_scope": 0.35, "autonomy": 0.30, "impact": 0.25, "exposure": 0.10}
    scores = {k: _score(agent, RISK_KEYWORDS[k]) for k in weights}
    weighted = sum(scores[k] * weights[k] for k in weights)

    if any(t in agent for t in HIGH_RISK_TRIGGER) and weighted >= 2.5:
        level = "高风险"
        note = "需 AI 治理委员会审批 + 红队测试 + 专项评估（06 模块 §2）"
    elif weighted >= 4.0:
        level = "高风险"
        note = "需 AI 治理委员会审批 + 红队测试 + 专项评估（06 模块 §2）"
    elif weighted >= 2.5:
        level = "中风险"
        note = "需部门+信息安全审批，半年度复审（06 模块 §2）"
    else:
        level = "低风险"
        note = "部门审批，登记即用（06 模块 §2）"

    print("=" * 62)
    print("Agent 风险清单与等级")
    print("=" * 62)
    print(f"Agent：{agent}")
    print(f"综合加权分：{weighted:.2f}（满分 5.00）")
    print("-" * 62)
    for k in weights:
        print(f"  {k}：{scores[k]} 分（权重 {int(weights[k]*100)}%）")
    print("-" * 62)
    print(f"风险等级：【{level}】")
    print(f"处理建议：{note}")
    print("\n六类风险自查（01 模块）：越权 / 逃逸 / 滥用 / 幻觉链 / 级联失败 / 不可追溯")
    print("建议按 03 模块检查权限与护栏，02 模块检查生命周期各阶段。")
    return 0


# ---------------------------------------------------------------- perm

def perm(tools, required):
    if not tools or not required:
        print("错误：--tools 与 --required 均必填，逗号分隔。")
        return 2
    tool_set = [t.strip() for t in tools.split(",") if t.strip()]
    req_set = [r.strip() for r in required.split(",") if r.strip()]

    def linked(t, r):
        # 双向包含即视为关联（如 "CRM" 与 "CRM读写"）
        return t in r or r in t

    extra = [t for t in tool_set if not any(linked(t, r) for r in req_set)]
    missing = [r for r in req_set if not any(linked(t, r) for t in tool_set)]

    print("=" * 62)
    print("Agent 权限评估（最小权限检查）")
    print("=" * 62)
    print(f"已配置工具：{'、'.join(tool_set)}")
    print(f"任务必需能力：{'、'.join(req_set)}")
    print("-" * 62)
    if extra:
        print(f"⚠️ 多余权限（建议移除/收窄）：{'、'.join(extra)}")
    else:
        print("✅ 未发现明显多余权限")
    if missing:
        print(f"⚠️ 能力缺口（任务必需但工具未覆盖）：{'、'.join(missing)}")
    else:
        print("✅ 必需能力均有工具覆盖")
    print("-" * 62)
    print("护栏检查（03 模块）：")
    print("  · 工具白名单   [ ] 只允许批准清单内工具")
    print("  · 参数强校验   [ ] 关键参数（收件人/金额/地址）校验")
    print("  · 操作分级     [ ] 只读自动，高风险写操作人工确认")
    print("  · 速率限制     [ ] 频率/批量限制")
    print("  · 熔断开关     [ ] 异常自动暂停转人工")
    return 0


# ---------------------------------------------------------------- maturity

DIMS = ["权限管理", "生命周期", "护栏控制", "责任分配", "监管合规", "监控审计"]


def maturity(scores_str):
    try:
        scores = [int(x.strip()) for x in scores_str.split(",")]
    except ValueError:
        print("错误：--scores 需为 6 个数字，逗号分隔，如 3,4,2,5,3,4")
        return 2
    if len(scores) != 6 or any(s < 1 or s > 5 for s in scores):
        print("错误：需 6 个 1-5 分，如 --scores 3,4,2,5,3,4")
        return 2
    total = sum(scores)
    print("=" * 62)
    print("Agent 治理成熟度自评（6 维度，每项 1-5 分）")
    print("=" * 62)
    for name, s in zip(DIMS, scores):
        bar = "█" * s + "░" * (5 - s)
        flag = " ← 短板" if s <= 2 else ""
        print(f"  {name}：{s} 分 {bar}{flag}")
    print("-" * 62)
    print(f"总分：{total} / 30")
    if total <= 12:
        stage, advice = "起步期", "先做 Agent 登记台账 + 最小权限检查（02/03 模块）。"
    elif total <= 23:
        weak = [n for n, s in zip(DIMS, scores) if s <= 2]
        stage = "建设期"
        advice = "补齐短板" + ("：" + "、".join(weak) + "。" if weak else "，优先权限与护栏。")
    else:
        stage, advice = "成型期", "体系化运转，保持季度复审与法规跟踪。"
    print(f"阶段判断：{stage}")
    print(f"改进建议：{advice}")
    return 0


# ---------------------------------------------------------------- liability

def liability(scene):
    if not scene or not scene.strip():
        print("错误：--scene 不能为空。示例：--scene \"Agent误发邮件给错误客户，含敏感信息\"")
        return 2
    print("=" * 62)
    print("Agent 事故责任分配建议（04 模块三线归因）")
    print("=" * 62)
    print(f"事故场景：{scene}")
    print("-" * 62)

    dev = "设计缺陷（算法/权限设计/注入防护缺失）→ 开发方担责" if any(
        k in scene for k in ["越权", "逃逸", "注入", "设计", "权限设计", "幻觉"]) else "无明确设计缺陷证据 → 开发方责任待评估"
    dep = "部署配置（权限过大/护栏未启/监控缺失/未做评估/敏感数据外发无拦截）→ 部署方担责" if any(
        k in scene for k in ["权限", "配置", "监控", "护栏", "未评估", "敏感", "沙箱", "人工确认"]) else "部署配置无明显过失 → 部署方责任待评估"
    use = "使用指令（超范围指令/误操作/未按监督要求/数据错误）→ 使用方担责" if any(
        k in scene for k in ["指令", "监督", "误用", "误发", "误操作", "数据错误", "超范围"]) else "使用环节无明显过失 → 使用方责任待评估"

    print(f"① {dev}")
    print(f"② {dep}")
    print(f"③ {use}")
    print("-" * 62)
    print("处置流程（06 模块 §3）：冻结 → 取证 → 分级 → 处置 → 归因 → 复盘")
    print("提醒：审计日志是责任划分关键证据；无日志 = 归因困难。")
    return 0


# ---------------------------------------------------------------- regulation

REGULATIONS = {
    "cn": [
        "《智能体规范应用与创新发展实施意见》（2026-05，网信办/发改委/工信部）——首个 Agent 顶层政策",
        "防越权：智能体权限边界管理，不得超出授权范围行动",
        "防逃逸：防止智能体绕过安全控制/沙箱/指令约束",
        "防滥用：防止智能体被用于违规、欺诈、数据滥用",
        "对外服务：安全评估 + 与算法备案/大模型备案衔接",
        "内容安全：Agent 生成内容纳入内容标识与审核要求",
        "未成年人保护：面向未成年人的智能体服务特殊要求",
    ],
    "sg": [
        "模型 AI 治理框架 Agentic AI 版（2026-05，IMDA/PDPC）——全球首个国家级 Agent 治理框架",
        "问责与监督：明确部署方问责义务与人工监督点",
        "安全可靠：Agent 失败模式（越权/幻觉）安全要求",
        "透明度：Agent 自主行动的可见性与可解释性",
        "数据保护：PDPA 合规（同意/目的限制/72 小时泄露通报）",
        "测试：AI Verify 延伸至 Agent 场景（政府采购趋近半强制）",
    ],
    "intl": [
        "欧盟：AI Act 按系统监管，Agent 执行高风险场景触发高风险义务；GPAI 规则（2026-08-02 全面执法）覆盖底层模型",
        "欧盟：关注 AI Act 年度评估对 Agent 透明度/记录义务的延伸",
        "美国：NIST AI Agent Standards Initiative（2026-01）将 AI RMF 延伸至自主智能体",
        "美国：COSAiS 控制覆盖层（单/多 Agent 系统）草案中",
        "通用：Agent 部署方建立登记台账 + 权限最小化 + 红队测试 + 日志审计 + 熔断",
        "通用：责任合同与保险前置约定（04 模块）",
        "通用：季度跟踪各地 Agent 监管进展",
    ],
}


def regulation(region):
    if region not in REGULATIONS:
        print("错误：--region 仅支持 cn（中国）/ sg（新加坡）/ intl（国际）。")
        return 2
    names = {"cn": "中国", "sg": "新加坡", "intl": "国际（欧盟+美国+通用）"}
    print(f"{'=' * 62}")
    print(f"{names[region]} Agent 监管要点速查")
    print(f"{'=' * 62}")
    for i, s in enumerate(REGULATIONS[region], 1):
        print(f"  {i}. {s}")
    print("\n[说明] 核对基准日 2026-08-27；落地以官方原文为准（详见 05 模块）。")
    return 0


# ---------------------------------------------------------------- main

def main():
    parser = argparse.ArgumentParser(
        prog="agent_gov_toolkit",
        description=f"AI 智能体治理本地工具包 v{VERSION}（零网络、零数据采集，仅标准库）",
    )
    sub = parser.add_subparsers(dest="command")

    p_risk = sub.add_parser("risk", help="Agent 风险清单与等级")
    p_risk.add_argument("--agent", required=True, help="Agent 描述")

    p_perm = sub.add_parser("perm", help="权限评估（最小权限检查）")
    p_perm.add_argument("--tools", required=True, help="已配置工具清单，逗号分隔")
    p_perm.add_argument("--required", required=True, help="任务必需能力，逗号分隔")

    p_mat = sub.add_parser("maturity", help="治理成熟度自评")
    p_mat.add_argument("--scores", required=True, help="6 个维度 1-5 分，逗号分隔")

    p_lia = sub.add_parser("liability", help="责任分配建议")
    p_lia.add_argument("--scene", required=True, help="事故场景描述")

    p_reg = sub.add_parser("regulation", help="监管要点速查")
    p_reg.add_argument("--region", required=True, choices=["cn", "sg", "intl"], help="cn=中国 / sg=新加坡 / intl=国际")

    args = parser.parse_args()

    if args.command == "risk":
        return risk(args.agent)
    if args.command == "perm":
        return perm(args.tools, args.required)
    if args.command == "maturity":
        return maturity(args.scores)
    if args.command == "liability":
        return liability(args.scene)
    if args.command == "regulation":
        return regulation(args.region)

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
