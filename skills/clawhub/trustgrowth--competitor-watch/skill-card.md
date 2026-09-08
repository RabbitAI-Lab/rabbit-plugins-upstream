## Description:

Use when the user wants competitor comparison or movement. Supports TrustGrowth history, cost-gated DataForSEO observations, and validated imports while separating snapshots from persisted tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and SEO teams use this skill to compare competitors, distinguish snapshots from tracked movement, and prepare evidence-labeled observations about rankings, gaps, and link profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid SEO providers or indexes can create cost exposure.

Mitigation: Require bounded cost approval before paid DataForSEO or paid-index requests.

Risk: Provider credentials may expose data or paid services when used unintentionally.

Mitigation: Confirm credentials and local read-only MCPs are intentionally configured before use, and never print secrets.

Risk: Third-party SEO data is estimated and may be mistaken for private measurement.

Mitigation: Label third-party observations as estimates and preserve source, date, and limitation notes in reports.

Risk: A point-in-time snapshot can be misread as competitor movement.

Mitigation: Only describe movement when compatible historical observations exist; otherwise report the current snapshot and name the missing history.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [Competitor Watch on ClawHub](https://clawhub.ai/trustgrowth/skills/competitor-watch)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and concise guidance with evidence labels]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source, date, cost, and limitation labels; paid connector use requires explicit cost approval.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
