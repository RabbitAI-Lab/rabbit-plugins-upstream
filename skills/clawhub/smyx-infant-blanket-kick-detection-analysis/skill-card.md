## Description:

Analyzes infant crib videos for blanket coverage and kicking events, returning alerts and links to cloud reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use the skill to review infant crib videos for blanket displacement alerts and consult past analysis reports. Its alerts supplement, rather than replace, direct adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant footage or video URLs are sent to lifeemergence cloud services.

Mitigation: Obtain guardian consent and use the skill only if cloud processing of the footage is acceptable.

Risk: The skill automatically creates a cloud-linked identity and stores tokens in workspace data.

Mitigation: Review before installation, limit access to workspace data, and remove it when the identity and tokens are no longer needed.

Risk: The cloud service may fetch a supplied video URL.

Mitigation: Avoid internal or private URLs; provide only video URLs intended for cloud access.

Risk: Automated blanket alerts can be mistaken for direct supervision.

Mitigation: Treat results as supplementary and check on the infant directly when an alert occurs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-blanket-kick-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured text reports with JSON results and Markdown links to cloud reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list past reports and save results to a local file.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
