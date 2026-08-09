## Description:

This skill helps agents produce disciplined A-share short-term stock screening reports using quote snapshots, K-line history, announcement checks, and manual checklist review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handm-735](https://clawhub.ai/user/handm-735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to screen A-share short-term trading candidates, check a named stock against the 96-principle checklist, and produce a structured pre-trade or holding review. The outputs are screening and discipline aids, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill outputs stock screening guidance that could be mistaken for investment advice.

Mitigation: Treat outputs as educational screening material only and require human review before any trading decision.

Risk: Market snapshots and delayed data can become stale, especially for a 14:30 short-term workflow.

Mitigation: Refresh quote and K-line data near the intended review time and include the data timestamp in the report.

Risk: Announcement checks may be unreliable when a data source is not scoped to the requested stock.

Mitigation: Use the script's scoped-data warning and manually verify major-holder reduction, earnings, penalty, or delisting signals against authoritative announcement pages.

Risk: The skill contacts public Chinese finance data sources and batch screening can create candidates.json.

Mitigation: Run it only in an environment where those public network calls and local output files are expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handm-735/skills/kline-shortterm-checklist)
- [Checklist methodology](artifact/references/checklist.md)
- [K-line pattern rules](artifact/references/kline_patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown screening report with optional JSON-prefixed script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch screening may write candidates.json in the current working directory.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
