## Description:

Generates daily, weekly, monthly, or yearly agent usage and cost reports from local activity records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Agent users and developers analyze local WorkBuddy, Claude Code, Codex, and Qwenwork histories to track tokens, estimated costs, tasks, and usage trends. The dumate source reads WorkBuddy-layout data but does not establish DuMate attribution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local agent histories and generated reports can expose private prompts, project paths, task labels, file names, and costs.

Mitigation: Grant access only to intended local histories; keep generated reports private and review them before sharing.

Risk: HTML reports made from untrusted or imported logs may allow content injection through unescaped model names.

Mitigation: Avoid opening or sharing HTML reports from untrusted logs until the escaping flaw is fixed; use text or JSON output when appropriate.

Risk: Pricing configuration can be written or changed, affecting cost estimates.

Mitigation: Review the exact models and prices before allowing changes to pricing.local.json or pricing.json; compare estimated costs with actual bills.

Risk: The dumate source may read WorkBuddy data without proving it belongs to DuMate.

Mitigation: Confirm data provenance before attributing dumate reports to DuMate usage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data sources](artifact/references/data_sources.md)
- [Adapter documentation](artifact/docs/ADAPTERS.md)
- [Frequently asked questions](artifact/references/FAQ.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON]

**Output Format:** [Report summary and Markdown, HTML, or JSON report file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes token trends, estimated costs, task categories, and data-quality warnings; available sections depend on the data source.]

## Skill Version(s):

1.9.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
