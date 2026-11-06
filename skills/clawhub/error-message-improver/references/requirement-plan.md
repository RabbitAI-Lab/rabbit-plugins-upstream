# Requirement Plan

## Live Requirement

Validated demand: Users and support teams need clearer error messages that explain what failed, why it failed, and what action to take next. This requirement is supported by 12 separate online signals across 3 source families, so it represents broader demand rather than a single isolated request.

## Audience

application developers, support teams, SaaS operators, and users who lose time when vague errors block troubleshooting

## Category

work-productivity

## Requirement Score

Total: 100/100

Demand: 70/70

Local feasibility: 30/30

Evidence coverage: 12 signals across 3 source families.

Scoring rationale:

- Evidence count: 12; required minimum: 3.
- Distinct source families: 3; sources: github, hacker-news, segmentfault.
- Demand score: 70/70 based on corroboration, source diversity, and professional/community signal.
- Local feasibility score: 30/30.
- Implementation is a documentation, workflow, code, or analysis skill that can run on ordinary CPU hardware.

## Evidence

- github-issues (2026-10-23T03:53:12+00:00): [🤖 Claude 排程協調看板（請勿關閉）](https://github.com/YuanShuoHsu/biru-api/issues/5)
- github-issues (2026-10-30T11:41:25+00:00): [Remove all existing version tags and give every package one uniform development version line](https://github.com/swift-institute/institute/issues/236)
- github-issues (2026-11-04T16:51:53+00:00): [Fine-tune a small model on verified compile traces](https://github.com/TheMissenoOne/OpenArc/issues/63)
- github-issues (2026-11-02T10:19:49+00:00): [[Intake] free-stockdb 的 data1 目录是同步增量层，改名后查询会表现为近期数据"消失"（日k退回、分钟k退回、资金流为空），实际基线数据完好。改回 da](https://github.com/Ikalus1988/MisakaNet/issues/4339)
- segmentfault-search (2026-11-06T04:12:34.418000+00:00): [HarmonyOS 开发者社区](https://segmentfault.com/brand/harmonyos-next)
- segmentfault-search (2026-11-06T04:12:34.418000+00:00): [javascript](https://segmentfault.com/t/javascript)
- segmentfault-search (2026-11-06T04:12:34.418000+00:00): [typescript](https://segmentfault.com/t/typescript)
- segmentfault-search (2026-11-06T04:12:34.418000+00:00): [ONES 研发管理](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- segmentfault-search (2026-11-06T04:12:34.418000+00:00): [答： c++单例类编译不通过](https://segmentfault.com/q/1010000004886164/a-1020000004886445)
- segmentfault-search (2026-11-06T04:12:34.418516+00:00): [error-messages](https://segmentfault.com/t/error-messages)
- segmentfault-search (2026-11-06T04:12:34.418516+00:00): [问： vue自定义指令报错](https://segmentfault.com/q/1010000009322969)
- hacker-news-search (2026-11-04T03:55:15+00:00): [C++26 Disapproved](https://news.ycombinator.com/item?id=50361335)

## How The Skill Meets The Requirement

Transforms the live request into a repeatable workflow that clarifies the user's context, produces a concrete deliverable, checks the result against the original need, and keeps execution feasible on ordinary CPU or family GPU hardware.

## Executable Implementation Plan

1. Restate the user's outcome, constraints, available inputs, and success criteria.
2. Create a concise work plan, template, automation outline, or decision aid that reduces manual coordination.
3. Ask only for missing information that materially changes the output; otherwise make reasonable assumptions and continue.
4. Keep the implementation local-hardware friendly: prefer scripts, templates, checklists, and small-model or CPU-safe workflows over cloud-only or large-training approaches.
5. Produce the requested artifact, workflow, checklist, analysis, code change, or decision support.
6. Validate the output against the success criteria and list any remaining risks or follow-up work.

## Expected Outputs

- A tailored answer or artifact for the user's immediate situation.
- A reusable checklist or workflow when the task is repeatable.
- A verification note showing how the result was checked.

## Review Criteria

- The output directly addresses the discovered requirement.
- The user can act on the result without reading the original source post.
- Assumptions, limits, and required inputs are visible.
- The final response includes a short usage or next-step note when helpful.

## Usage Signals

Keywords: work-productivity, error messages, debugging, user feedback, support, troubleshooting

Trigger sentences:

- Help me Users and support teams need clearer error messages that explain what failed, why it failed, and what action to take nex.
- I need a practical workflow for Users and support teams need clearer error messages that explain what failed, why it failed, and what action to take nex.
- Use $error-message-improver to handle Users and support teams need clearer error messages that explain what failed, why it failed, and what action to take nex.
