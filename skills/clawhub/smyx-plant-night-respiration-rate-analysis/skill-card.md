## Description:

Estimates relative plant night respiration intensity from thermal canopy imagery and optional ambient CO2 signals for plant factories, climate chambers, and closed greenhouses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agricultural operators use this skill to analyze nighttime thermal plant imagery or video, estimate a relative respiration index, review metabolic activity levels, and retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and submitted URLs may be sent to a remote analysis service.

Mitigation: Use only approved plant media and URLs, and review or change the default endpoints before production use.

Risk: The skill may silently create or reuse a local identity and store tokens for future report history queries.

Mitigation: Provide an explicit cleanup or reset path for local identity and token data before production use.

Risk: History queries are account-linked and offer limited user control.

Mitigation: Confirm the expected account scope and user consent before enabling report history retrieval.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include respiration intensity, activity level, risk prompts, recommendations, report links, and Markdown tables for report history.]

## Skill Version(s):

1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
