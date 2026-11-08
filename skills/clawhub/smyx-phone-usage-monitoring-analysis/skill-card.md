## Description:

Analyzes workplace images and video to identify phone use and produce reports on frequency and duration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Employers and workplace operations teams use the skill to review supplied office images or video for apparent phone use and view frequency and duration summaries. Treat its results as management aids, not as the sole basis for disciplinary decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Upload destination overrides and configuration-only mode may not provide the advertised safeguards for employee footage.

Mitigation: Have the publisher fix and verify both controls before using employee footage. Confirm organizational authorization for the receiving service, its retention, and report access; begin with synthetic media.

Risk: The skill handles persistent credentials without clear user control.

Mitigation: Use a dedicated identity, protect the token database, and keep API secrets separate from user identifiers.

## Reference(s):

- [Workplace phone usage monitoring API documentation](artifact/references/api_doc.md)
- [Skill usage demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured report text or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include employee behavior counts, durations, recommendations, and report links.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
