## Description:

Generates monthly GEO delta reports by comparing baseline and current audits, calculating score changes, tracking action item completion, and producing client-facing progress reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[asale-ai](https://clawhub.ai/user/asale-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External agency teams and client-facing marketers use this skill to compare two GEO audits for a domain and create a monthly progress report showing score deltas, completed actions, wins, new issues, and next-month priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A valid delta report requires two audit points; using only one audit or running a fresh audit without confirmation can produce a weak or unintended comparison.

Mitigation: Prefer providing two explicit audit files or require confirmation before running a fresh audit, then verify that the baseline and current audit dates are correct.

Risk: Generated client reports can include estimated scores, business impact, and next-step priorities that may be inaccurate if the source audits are incomplete.

Mitigation: Review the generated calculations, assumptions, and recommendations before sharing the report with a client.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/asale-ai/skills/geo-compare)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown report plus concise text confirmation with key stats and a suggested next action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a monthly report file when used as authored and relies on baseline/current audit inputs or stored audit records.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
