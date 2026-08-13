#!/usr/bin/env python3
"""Deterministic router for self-evolving-memory evals.

The router selects a workflow only. It does not read or mutate a live memory
deployment. JSON is written to stdout for the skill-forge expectations DSL.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    workflow_bundle: str
    primary_module: str
    reason: str


EXPLICIT = re.compile(
    r"(\$self-evolving-memory|use\s+self-evolving-memory|用\s*self-evolving-memory)",
    re.IGNORECASE,
)
MEMORY_CONTEXT = re.compile(
    r"(AI\s*Agent|Agent|智能体|记忆系统|agent\s+memory|layered\s+memory|"
    r"self-evolving-memory|SECRET\.md|recent_memory|memory_search|SOUL\.md|MEMORY\.md|"
    r"记忆巩固|微巩固|回忆规划|证据账本|事件因果图谱|主题索引|检索校验|"
    r"评估晋升|主动探索|自我认知|技能建议冷却|分层存储|即时层|"
    r"(?:这条|某条|错误).{0,12}(?:记忆|memory)|搜.{0,8}记忆|记忆片段|"
    r"按主题聚合.{0,12}记忆|因果链.{0,12}记忆)",
    re.IGNORECASE,
)
SECURITY = re.compile(
    r"(SECRET\.md|明文凭证|secret\s+(handle|locator)|凭证迁移|"
    r"(?:API[ _-]?key|password|密码|token|私钥|cookie).{0,24}(?:迁移|轮换|撤销|locator|handle))",
    re.IGNORECASE,
)
TRANSACTION = re.compile(
    r"(并发巩固|共享锁|排他锁|write[- ]?set|事务|tombstone|preimage|恢复状态机|快照碰撞|部分提交)",
    re.IGNORECASE,
)
CONSOLIDATION = re.compile(
    r"(记忆巩固|跑一次巩固|每日巩固|四阶段巩固|微巩固|回滚记忆|快照恢复|SOUL\.md被改|SOUL\.md.*核心身份|巩固.{0,40}SOUL\.md|SOUL\.md.{0,40}巩固)",
    re.IGNORECASE,
)
INIT = re.compile(
    r"(初始化记忆系统|初始化.*Agent.*记忆|部署记忆|修复.*记忆系统|fresh init|existing deployment|缺少.*记忆文件|soul\.md.*growth-journal|即时层.*(20KB|容量|快满)|容量管理)",
    re.IGNORECASE,
)
CAPABILITY = re.compile(
    r"(没有|缺少|不支持|without).{0,16}(Calendar|memory_search|调度器|语义检索)|(Calendar|memory_search|调度器|语义检索).{0,16}(没有|缺少|不支持|不可用|fallback|降级)",
    re.IGNORECASE,
)
PROMOTION = re.compile(
    r"(评估晋升|该不该晋升|晋升.*打分|promotion score|证据门控|累计权重)",
    re.IGNORECASE,
)
EVIDENCE = re.compile(r"(证据账本|evidence ledger|可信的证据|整理.*证据)", re.IGNORECASE)
RECALL = re.compile(r"(回忆规划|recall planner|搜记忆之前|检索前.*拆解)", re.IGNORECASE)
CAUSAL = re.compile(r"(事件因果图谱|因果图谱|因果链|causal graph)", re.IGNORECASE)
TOPIC = re.compile(r"(主题实体索引|主题索引|按主题聚合)", re.IGNORECASE)
RETRIEVAL = re.compile(
    r"(记忆检索校验|检索校验|搜一次没找到|搜索记忆|搜记忆|memory_search|四级检索)",
    re.IGNORECASE,
)
DPM = re.compile(r"(DPM|Trace Forest|动态分层|动态自适应.*记忆|角色化记忆切片)", re.IGNORECASE)
EXPLORATION = re.compile(r"(主动探索|认知拉伸|盲区发现|熟悉的东西里打转)", re.IGNORECASE)
SELF_REFERENCE = re.compile(r"(自我认知|身份演化|关系理解|Agent反思自己|可演化的认知)", re.IGNORECASE)
COOLDOWN = re.compile(r"(技能建议冷却|反复.*建议|驳回.*建议|永久冷却)", re.IGNORECASE)
LIGHTWEIGHT = re.compile(
    r"(帮我记一下|请记住|记一下这条|记住这条|记住这个|赶紧记一下|remember this|lightweight record)",
    re.IGNORECASE,
)
ROLLBACK_MEMORY = re.compile(r"(回滚|撤销).{0,18}(错误|这条|某条|该条)?.{0,12}(记忆|memory)", re.IGNORECASE)
COOLDOWN_DIRECTIVE = re.compile(
    r"(拒绝|不要|别).{0,18}(同一|同一个).{0,18}(建议|推荐).{0,18}(两次|再次|重复)",
    re.IGNORECASE,
)


def has_memory_context(prompt: str) -> bool:
    """Return whether broad technical terms are grounded in agent-memory scope."""
    return bool(MEMORY_CONTEXT.search(prompt) or EXPLICIT.search(prompt))


def detect(text: str) -> dict[str, object]:
    prompt = text.strip()
    route: Route | None = None

    # Broad technical vocabulary is only meaningful after an agent-memory scope
    # signal. This keeps database credentials, token validation, and UI menus
    # outside this skill while retaining explicit secret-migration requests.
    memory_scoped = has_memory_context(prompt)

    # Security and transaction boundaries win over broader module keywords.
    if SECURITY.search(prompt) and (memory_scoped or re.search(r"(SECRET\.md|明文凭证|凭证迁移)", prompt, re.IGNORECASE)):
        route = Route("security_migration", "01-layered-storage", "secret-boundary")
    elif TRANSACTION.search(prompt) and memory_scoped:
        route = Route("consolidation", "03-consolidation-guard", "transaction-safety")
    elif ROLLBACK_MEMORY.search(prompt):
        route = Route("consolidation", "03-consolidation-guard", "memory-rollback")
    elif CONSOLIDATION.search(prompt) and memory_scoped:
        primary = "09-consolidation-manual" if re.search(r"(完整|四阶段|阶段0|阶段 0)", prompt) else "03-consolidation-guard"
        route = Route("consolidation", primary, "consolidation-lifecycle")
    elif INIT.search(prompt) and memory_scoped:
        route = Route("init", "01-layered-storage", "init-or-repair")
    elif CAPABILITY.search(prompt) and memory_scoped:
        route = Route("capability_fallback", "01-layered-storage", "optional-host-capability-missing")
    elif EVIDENCE.search(prompt) and memory_scoped:
        route = Route("retrieval", "12-evidence-ledger", "evidence-ledger")
    elif RECALL.search(prompt) and memory_scoped:
        route = Route("retrieval", "13-recall-planner", "recall-planning")
    elif CAUSAL.search(prompt) and memory_scoped:
        route = Route("retrieval", "06-event-causality-graph", "causal-graph")
    elif TOPIC.search(prompt) and memory_scoped:
        route = Route("retrieval", "07-topic-entity-index", "topic-index")
    elif RETRIEVAL.search(prompt) and memory_scoped:
        route = Route("retrieval", "08-retrieval-verification", "retrieval-loop")
    elif PROMOTION.search(prompt) and memory_scoped:
        route = Route("promotion", "04-promotion-protocol", "promotion-evaluation")
    elif DPM.search(prompt) and (memory_scoped or re.search(r"(DPM|Trace Forest|角色化记忆切片)", prompt, re.IGNORECASE)):
        route = Route("growth", "11-dpm-enhancement", "dpm-enhancement")
    elif EXPLORATION.search(prompt) and memory_scoped:
        route = Route("growth", "10-active-exploration", "active-exploration")
    elif SELF_REFERENCE.search(prompt) and memory_scoped:
        route = Route("growth", "02-self-reference", "self-reference")
    elif COOLDOWN_DIRECTIVE.search(prompt):
        route = Route("consolidation", "05-skill-suggestion-cooldown", "recommendation-cooldown")
    elif COOLDOWN.search(prompt) and memory_scoped:
        route = Route("consolidation", "05-skill-suggestion-cooldown", "suggestion-cooldown")
    elif LIGHTWEIGHT.search(prompt):
        route = Route("lightweight_record", "01-layered-storage", "one-shot-record")
    elif EXPLICIT.search(prompt):
        route = Route("scope_clarification", "SKILL", "explicit-skill-invocation")

    if route is None:
        return {
            "should_trigger": False,
            "archetype": "mentor",
            "workflow_bundle": "out_of_scope",
            "primary_module": None,
            "reason": "no-memory-system-lifecycle-signal",
        }

    return {
        "should_trigger": True,
        "archetype": "mentor",
        "workflow_bundle": route.workflow_bundle,
        "primary_module": route.primary_module,
        "reason": route.reason,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Route a self-evolving-memory request")
    parser.add_argument("--text", required=True, help="User prompt")
    args = parser.parse_args()
    json.dump(detect(args.text), sys.stdout, ensure_ascii=False, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
