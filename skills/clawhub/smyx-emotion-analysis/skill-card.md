## Description:

Analyzes facial videos supplied as files or URLs and returns micro-expression and emotion reports with links to cloud-stored results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users submit facial videos or URLs for emotion-analysis reports and retrieve their cloud-stored report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face videos or URLs are sent to the publisher's cloud service.

Mitigation: Use only media you are authorized to process; avoid sensitive or non-consenting subjects.

Risk: The skill silently creates or reuses an identity and associates reports with it.

Mitigation: Review the publisher's identity, report access, and retention practices before use.

Risk: Service authentication tokens are stored in a local workspace database.

Mitigation: Restrict workspace access and remove stored tokens when they are no longer needed.

Risk: Facial-expression analysis may not reliably establish someone's inner emotional state.

Mitigation: Treat results as indicative only, not as a diagnosis or sole basis for consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [Emotion analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured report text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links; results can be saved to a file.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
