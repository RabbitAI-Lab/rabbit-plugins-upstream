# Requirement Plan

## Live Requirement

Validated demand: Teams need repeatable help adding useful unit tests and raising test coverage for existing codebases. This requirement is supported by 12 separate online signals across 3 source families, so it represents broader demand rather than a single isolated request.

## Audience

software maintainers, QA engineers, open-source contributors, and product teams who need confidence that changes do not break existing behavior

## Category

software-and-data

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

- github-issues (2026-09-02T17:25:20+00:00): [[SIA][W02] Establish collector, clock, metric and capability architecture](https://github.com/davecrawley/sia/issues/14)
- github-issues (2026-09-03T00:20:39+00:00): [[Relationships][Friend][FFR-06] Prove real Mac↔Windows Friend walk on current exact source](https://github.com/vgong24/VexLife/issues/379)
- github-issues (2026-09-02T03:08:11+00:00): [MASTER: Web Pilot capability-gap and production-readiness program](https://github.com/ORCHORDS/OrchordsBrowserPilot/issues/9)
- github-issues (2026-09-02T03:20:26+00:00): [P0: Harden Streamable HTTP against DNS rebinding, hostile origins, request abuse, and unsafe exposure](https://github.com/ORCHORDS/OrchordsBrowserPilot/issues/43)
- hacker-news-ask-hn (2026-09-05T18:38:11+00:00): [User-guide-driven development with coding agents](https://news.ycombinator.com/item?id=49579372)
- github-issues (2026-09-06T03:41:25+00:00): [Add agy (Antigravity CLI) as a third TuvalAiAgent backend, Pi-shaped and kernel-tool-free](https://github.com/kamp-us/phoenix/issues/8162)
- hacker-news-search (2026-08-25T13:35:21+00:00): [We had a unit test once which only failed on Sundays (2015)](https://qntm.org/unit)
- segmentfault-search (2026-09-06T04:05:05.176721+00:00): [HarmonyOS 开发者社区](https://segmentfault.com/brand/harmonyos-next)
- segmentfault-search (2026-09-06T04:05:05.176721+00:00): [javascript](https://segmentfault.com/t/javascript)
- segmentfault-search (2026-09-06T04:05:05.176721+00:00): [typescript](https://segmentfault.com/t/typescript)
- segmentfault-search (2026-09-06T04:05:05.176721+00:00): [ONES 研发管理](https://ones.cn/?utm_term=ONES%C2%A0%E7%A0%94%E5%8F%91%E7%AE%A1%E7%90%86&utm_campaign=%E9%A6%96%E9%A1%B5%E6%A0%87%E7%AD%BE&_channel_track_key=myqX1C0f&utm_source=%E6%80%9D%E5%90%A6%E8%BD%AC%20ONES)
- segmentfault-search (2026-09-06T04:05:05.176721+00:00): [Writing Great Unit Tests: Best and Worst Practices](https://segmentfault.com/a/1190000009709754)

## How The Skill Meets The Requirement

Transforms the live request into a repeatable workflow that clarifies the user's context, produces a concrete deliverable, checks the result against the original need, and keeps execution feasible on ordinary CPU or family GPU hardware.

## Executable Implementation Plan

1. Restate the user's outcome, constraints, available inputs, and success criteria.
2. Inspect technical constraints, propose implementation steps, and include test or verification commands when code or data is involved.
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

Keywords: software-and-data, unit tests, test coverage, testing, regression, quality

Trigger sentences:

- Help me Teams need repeatable help adding useful unit tests and raising test coverage for existing codebases.
- I need a practical workflow for Teams need repeatable help adding useful unit tests and raising test coverage for existing codebases.
- Use $unit-test-coverage-helper to handle Teams need repeatable help adding useful unit tests and raising test coverage for existing codebases.
