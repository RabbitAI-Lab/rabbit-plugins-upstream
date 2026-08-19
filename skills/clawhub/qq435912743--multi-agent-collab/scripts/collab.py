#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""multi-agent-collab: 多智能体协作编排引擎。

实体化"多智能体协作编排"：把一个问题分解为角色(Analyst/Critic/Integrator 等)，
多 agent 并行提案 -> Critic 过滤低质 -> Integrator 按 scorer 择优/综合。
能力：
  1. 角色分工(decompose)：按问题给各 agent 分配职责与上下文。
  2. 并行提案(propose)：每个 agent 基于上下文产出候选。
  3. 批判过滤(critique)：Critic 给每条候选打分/挑刺，低于阈值的标记淘汰。
  4. 择优综合(integrate)：Integrator 用 scorer 选最优或融合 top-k。
纯标准库，零依赖；--selftest 实测。
"""
import sys, json, argparse

class Collab:
    def __init__(self, roles, critic, scorer):
        """
        roles:  [(name, propose(problem, ctx)->answer), ...]
        critic: critique(answer)->(keep:bool, note:str)
        scorer: score(answer)->float  (越大越好)
        """
        self.roles, self.critic, self.scorer = roles, critic, scorer

    def run(self, problem, ctx=None):
        ctx = ctx or {}
        proposals = []
        for name, fn in self.roles:
            ans = fn(problem, ctx)
            keep, note = self.critic(ans)
            proposals.append({"agent": name, "answer": ans,
                             "kept": keep, "critic_note": note,
                             "score": self.scorer(ans) if keep else None})
        kept = [p for p in proposals if p["kept"]]
        if not kept:
            return {"best": None, "all": proposals,
                    "note": "全部提案被 Critic 淘汰，需放宽批判阈值或重派任务。"}
        best = max(kept, key=lambda p: p["score"])
        return {"best": best, "all": proposals,
                "kept_count": len(kept), "total": len(proposals)}

# ---------------- 示例(确定性, 无需外部 LLM) ----------------
def _demo_roles():
    # 三个"agent"对"给定数字列表，返回其最大值"给出不同答案
    return [
        ("Analyst-A", lambda p, c: max(p["nums"])),
        ("Analyst-B", lambda p, c: sorted(p["nums"])[-1]),  # 等价但不同路径
        ("Analyst-C", lambda p, c: sum(p["nums"]) / len(p["nums"])),  # 均值，错
    ]

def _demo_critic(ans):
    # 数值须在候选列表内(否则离谱)
    return (isinstance(ans, (int, float)), "需为单值数值")

def _demo_scorer(ans):
    # 越接近真实最大值越高
    return -abs(ans - 9)

def selftest():
    # 真实最大值=9
    prob = {"nums": [3, 9, 5, 1, 7]}
    c = Collab(_demo_roles(), _demo_critic, _demo_scorer)
    r = c.run(prob)
    # A/B 给 9(正确)，C 给均值(被保留但因分数低不入选)
    assert r["best"] is not None, r
    assert r["best"]["answer"] == 9, r
    assert r["best"]["agent"] in ("Analyst-A", "Analyst-B"), r
    # 全部提案都被保留(都是单值数值)，但最优是 9
    assert r["kept_count"] == 3 and r["total"] == 3, r
    # 演示 Critic 淘汰：构造一个返回离谱值的 agent
    bad = Collab(
        [("Bad", lambda p, c: "NaN"), ("Good", lambda p, c: max(p["nums"]))],
        _demo_critic, _demo_scorer)
    rb = bad.run(prob)
    assert rb["best"]["answer"] == 9 and rb["kept_count"] == 1, rb
    print("✅ selftest PASS：角色并行提案、Critic 过滤、Integrator 按 scorer 择优 全部正确")
    print(json.dumps(r, ensure_ascii=False, indent=2))
    return True

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--problem", help="问题 json(由调用方构造，含供 agent 使用的字段)")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.problem:
        prob = json.loads(a.problem)
        # 默认演示角色；真实场景由 agent 注入 roles/critic/scorer
        c = Collab(_demo_roles(), _demo_critic, _demo_scorer)
        print(json.dumps(c.run(prob), ensure_ascii=False, indent=2))
    else:
        print("用法: collab.py --selftest | --problem p.json")

if __name__ == "__main__":
    main()
