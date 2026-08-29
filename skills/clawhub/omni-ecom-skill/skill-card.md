## Description:

全域电商经营专家团 v1.5.11；用于店铺诊断、周报/月报/年报、大促复盘和投流利润分析。所有数字必须有来源，公式和归因范围必须通过数字闸门。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gzbarry1980-bot](https://clawhub.ai/user/gzbarry1980-bot)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators and analysts use this skill to review uploaded marketplace reports, lock metric definitions, diagnose store performance, analyze campaign and advertising economics, and prepare reviewable weekly, monthly, annual, diagnosis, and campaign recap reports. It emphasizes sourced numbers, formula checks, attribution boundaries, expert handoffs, approval gates, and final delivery receipts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local e-commerce reports that may contain sensitive customer, sales, advertising, refund, and operations data.

Mitigation: Use a clearly scoped run, provide only the reports needed for the task, keep private client-name registries local, and run the public-output guard before sharing results.

Risk: Business recommendations for budgets, campaigns, content, or operations could be incorrect if source data is incomplete or attribution scopes are mixed.

Mitigation: Require data-quality gates, source-backed numeric claims, formula and attribution checks, and explicit human approval before any operational action.

Risk: Multi-agent coordination can produce incomplete or stale deliverables if handoffs, reviews, or generated report files change during a run.

Mitigation: Use sealed handoffs, review attempts, frozen report hashes, PDF verification, and completion receipts before treating a delivery as final.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gzbarry1980-bot/skills/omni-ecom-skill)
- [README](artifact/README.md)
- [Context Isolation](artifact/skills/ecom-diagnosis-core/references/context-isolation.md)
- [Data Quality Gate](artifact/skills/ecom-diagnosis-core/references/data-quality-gate.md)
- [Evidence and Decision](artifact/skills/ecom-diagnosis-core/references/evidence-and-decision.md)
- [Metric Contract](artifact/skills/ecom-diagnosis-core/references/metric-contract.md)
- [Report Package Contract](artifact/skills/ecom-diagnosis-core/references/report-package-contract.md)
- [PDF Layout Style Master](artifact/skills/ecom-report-pdf-layout/references/style-master.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus structured JSON, Markdown report packages, PDF delivery artifacts, receipts, validation outputs, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided e-commerce reports and explicit customer scope; formal delivery depends on data-quality, claim, review, PDF, privacy, and completion gates.]

## Skill Version(s):

1.5.11 (source: evidence.release.version, artifact/version-info.json, artifact/.codebuddy-plugin/plugin.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
