# Industry Deep-Dive Pipeline

> Turn a topic brief, research materials, vendor case, policy event, or industry question into a publish-ready single deep-dive article — with source verification, originality review, full editorial planning, two human gates, deterministic red-line checks, and an eight-role review panel.

[![ClawHub](https://img.shields.io/badge/ClawHub-industry--deep--dive--pipeline--skill-blue)](https://clawhub.ai/haiyangchenbj/industry-deep-dive-pipeline-skill)
[![GitHub](https://img.shields.io/badge/GitHub-haiyangchenbj-black)](https://github.com/haiyangchenbj/industry-deep-dive-pipeline-skill)

---

## What it does

A fixed Prompt-Chaining + Evaluator-Optimizer pipeline that takes a single technology / AI / data / cloud / enterprise-software topic from brief to an approved final Markdown. The fixed main chain guarantees traceability; a revision loop after an eight-role panel review guarantees quality.

## When to use

- You have a topic brief, event, vendor case, policy change, or research material that needs a judgment-led, evidence-backed, boundary-clear deep-dive.
- You need pre-body planning (reader, core judgment, argument chain, counter-arguments, structure, title, risk) and a complete evidence package.

## When not to use

- News flashes, summaries, product manuals, tutorials, or marketing copy.
- Vendor conference panorama reports → use `vendor-summit-report`.
- LinkedIn single-platform short observations → use `linkedin-industry-observation`.
- WeChat layout / covers / publishing → hand off to the independent publishing suite.

## Pipeline at a glance

1. Diagnose input → 2. Build fact table → 3. Originality & competition review → 4. Planning brief → **Gate A (human)** → 5. Draft → 6. Machine red-line gate → 7. Eight-role review → **Gate B (human)** → 8. Revise → 9. Re-check → 10. Package.

## Hard rules (key)

- Search is for discovery; key facts return to primary sources.
- "Original / first / only" judgments need search evidence and boundaries.
- No body writing before Gate A; Gate B handles only genuine value tensions.
- Output stops at approved final + evidence package — never auto-publishes.

## File structure

```
industry-deep-dive-pipeline/
├── SKILL.md
├── SKILL_zh.md
├── README.md
├── README_zh.md
├── _meta.json
├── references/
│   ├── planning-schema.md
│   ├── evidence-and-originality.md
│   ├── writing-profile-interface.md
│   └── replay-evaluation.md
├── scripts/
│   ├── validate_case_bundle.py
│   └── scan_draft_gates.py
└── templates/
    ├── case-brief.template.md
    ├── fact-table.template.md
    ├── planning-brief.template.md
    ├── review-record.template.md
    └── final-package.template.md
```

## License

MIT
