## Description:

Analyzes in-home video of older adults living alone for behaviors such as prolonged inactivity, sighing, and self-talk, and provides emotional-risk reports for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Families and community caregivers use reports on in-home behavior to decide when to check in with an older adult living alone; reports are not a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive in-home video or audio and report history are sent to cloud services.

Mitigation: Obtain the monitored person's informed consent before use, and confirm who can access stored reports and exports.

Risk: The skill creates or reuses identity records and stores reusable authentication tokens locally.

Mitigation: Protect access to the local workspace database and restrict access to stored credentials.

Risk: Observed behavior can be mistaken for depression or loneliness.

Mitigation: Treat risk alerts as prompts for human follow-up, not as a diagnosis or replacement for professional assessment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-elderly-loneliness-depression-analysis)
- [Analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [JSON or Markdown report with behavior indicators, risk alerts, recommendations, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can list historical reports and save analysis results to a file.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
