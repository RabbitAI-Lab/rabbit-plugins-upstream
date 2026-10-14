## Description:

Analyzes adult face images or short videos for visible fatigue markers and provides a 0–100 fatigue/stress score with general suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and workplace wellness teams use adult face images or short videos to review a visual fatigue/stress estimate, general suggestions, and previous reports. Results are not medical diagnoses or clinical stress assessments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive adult face images or videos are sent to a configured cloud service.

Mitigation: Obtain the person's consent before use and confirm the service's retention and deletion practices before submitting sensitive or third-party media.

Risk: The skill may silently create or reuse a local/cloud identity and retain local tokens and report history.

Mitigation: Disclose the identity and storage behavior before use, check where tokens and reports persist, and establish a way to clear them.

## Reference(s):

- [Analysis API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-adult-facial-fatigue-stress-index-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report text or JSON; historical reports as a Markdown table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a 0–100 score, fatigue category, observed features, suggestions, and a report link; output can be saved to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; artifact frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
