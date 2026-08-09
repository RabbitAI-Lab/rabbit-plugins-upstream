## Description:

Detects possible falls in video streams or uploaded video files and returns a structured fall-detection report for elderly home safety monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to analyze local video files or video URLs for suspected falls, review structured reports, and query cloud-stored history for home safety monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive fall-detection media may be processed by cloud services.

Mitigation: Use consented test media when possible and avoid uploading private home footage unless monitored individuals have authorized that use.

Risk: The skill may create or reuse an internal identity and store authentication tokens locally.

Mitigation: Run the skill in a dedicated workspace or account and review local credential handling before production use.

Risk: Cloud report history lookup and limited user control over processing may be unsuitable for some deployments.

Mitigation: Deploy only where cloud processing, report history, and account behavior match the operator's privacy and governance requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown/plain text reports with structured JSON-style analysis content and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs; supports history-list output and optional result file writing.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
