## Description:

Combines facial blood flow and emotional characteristics to analyze stress index, anxiety tendency, and depression tendency for mental health monitoring scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit face image or video inputs and receive structured psychological stress, anxiety tendency, and depression tendency assessment reports for wellness monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images or videos and psychological assessment results may be transmitted to external services.

Mitigation: Use only with explicit user consent and avoid real personal or clinical data until destinations, retention, deletion, and access controls are documented.

Risk: Plaintext development endpoints or HTTP service URLs may expose sensitive data or tokens.

Mitigation: Require HTTPS production endpoints and remove or disable local development endpoints before deployment.

Risk: Silent account creation and persistent local token storage reduce user transparency and control.

Mitigation: Require visible consent, identity controls, and a documented local token cleanup process before use.

Risk: Cloud history queries may retrieve prior psychological assessment reports.

Mitigation: Limit history access to authorized identities and review returned report links before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown or JSON report text, with optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stress, anxiety tendency, depression tendency, recommendations, history records, and report export links.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
