## Description:

Detects the appearance of strangers near minors and actively issues safety reminder alerts to protect minor safety, suitable for homes, schools, childcare centers, and other scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze surveillance images, videos, or URLs for possible strangers near minors and to retrieve structured warning reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive surveillance media or URLs may be sent to a remote backend.

Mitigation: Use the skill only with authority and consent to process the footage, especially when minors may appear.

Risk: Cloud report history can be retrieved by the skill.

Mitigation: Confirm report access, retention, and backend policies before deployment.

Risk: The skill creates or reuses local or remote identity state with stored tokens.

Mitigation: Review identity and token handling before installation and limit use to acceptable environments.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-stranger-approach-warning-analysis)

## Skill Output:

**Output Type(s):** [analysis, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file when requested.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
