## Description:

Fund CIO Copilot helps industrial fund teams screen business plans, prepare investment evaluations and IC packages, monitor portfolio decisions, and generate local state-owned investment radar reports while keeping final investment decisions with human reviewers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[perrykono-debug](https://clawhub.ai/user/perrykono-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Investment managers, IC members, and industrial fund operators use this agent to route work across screening, evaluation, IC, portfolio review, and radar-report modes. It organizes evidence, gates, recommendations, decision objects, and institutional memory for human investment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retain sensitive investment records, mandates, outcomes, learning notes, and radar benchmarks in the workspace.

Mitigation: Install and run it only in a workspace approved for confidential investment records, and define access, retention, deletion, and export controls before use.

Risk: Radar workflows may create external Tencent Docs containing generated investment intelligence.

Mitigation: Confirm that external document creation is authorized, apply the skill's redaction rules for external or training copies, and review content before sharing.

Risk: Investment recommendations or IC materials could be mistaken for final investment decisions.

Mitigation: Require human IC review for all investment decisions and preserve the skill's mandatory disclaimer that outputs are analysis suggestions, not investment decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/perrykono-debug/skills/fund-cio-copilot)
- [Skill Definition](artifact/SKILL.md)
- [Decision Object Schema](artifact/decision-object.md)
- [Decision Memory](artifact/decision-memory.md)
- [Investment Mandate](artifact/mandate.md)
- [Weekly Radar Mode](artifact/mode-weekly-radar.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Configuration, Guidance]

**Output Format:** [Markdown reports, structured JSON decision objects, local memory/configuration files, and guidance text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May retain decision, outcome, learning, mandate, and radar benchmark records in the workspace; Radar mode may create Tencent Docs when configured.]

## Skill Version(s):

2.6.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
