## Description:

Analyzes aquatic pet videos from files or URLs and returns health findings, potential disease warnings, and care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers and their assistants use this skill to review aquatic pet videos for possible health concerns and retrieve previous reports. Results are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquatic pet media or URLs, an internal identity value, and report queries are sent to the lifeemergence.com backend.

Mitigation: Confirm the destination and obtain user approval before sending content or querying cloud reports.

Risk: The skill silently creates or signs in to an account, persists authentication tokens locally, and can access cloud history.

Mitigation: Review identity and token storage behavior and restrict access to accounts and report history before use.

Risk: The autism_analysis and AUTISM_ANALYSIS references conflict with the aquarium analysis workflow.

Mitigation: Check the actual command and analysis scenario before execution; require fixes if they route to the wrong analysis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [Aquatic health analysis API reference](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or structured JSON health findings; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and optionally save results to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata; packaged frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
