## Description:

Analyzes pet monitoring videos or images for feeding, drinking, excretion, mental state, vomiting, limping, and other health indicators, then returns structured health monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet camera or feeder monitoring media, detect health-related behavior patterns or abnormalities, and retrieve structured monitoring reports or report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-monitoring videos, video URLs, report requests, and account-linked identifiers may be sent to configured lifeemergence.com services.

Mitigation: Review service endpoints and obtain explicit user confirmation before analyzing media or querying cloud report history.

Risk: The skill silently creates or reuses a local identity and stores token records in a local SQLite database.

Mitigation: Confirm local storage of workspace identity and token data is acceptable, and remove local data when the workspace should not retain account-linked state.

Risk: Health reports are reference material and may be incomplete or incorrect for clinical decisions.

Mitigation: Present results as pet health guidance only and direct users to a veterinarian when abnormalities or urgent symptoms are detected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-pet-health-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON reports, with optional shell commands for invoking bundled scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include health indicators, warnings, care suggestions, report links, and Markdown tables for history queries.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter declares 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
