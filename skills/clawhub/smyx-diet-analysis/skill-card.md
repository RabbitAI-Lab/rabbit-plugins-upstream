## Description:

Analyzes meal videos and images to evaluate eating behavior, dietary habits, and diet structure, then returns structured reports and nutrition improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit meal media for dietary behavior analysis, including eating speed, eating habits, diet structure, and risk behavior screening. The skill can also retrieve cloud-hosted historical analysis reports for the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Eating-related images or videos are uploaded to a cloud service for analysis.

Mitigation: Use only with appropriate consent and avoid submitting identifiable or sensitive media unless cloud processing is acceptable.

Risk: The skill automatically creates or reuses an identity and stores local authentication tokens in the workspace data directory.

Mitigation: Review workspace data access before installation and rotate or remove local tokens when access changes.

Risk: Broad history-report requests can query prior cloud records for the resolved identity.

Mitigation: Run history/list commands only for authorized users and confirm the account context before displaying prior reports.

Risk: Packaged development HTTP endpoint configuration is present alongside production endpoints.

Mitigation: Confirm production HTTPS endpoint configuration before handling sensitive media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-diet-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text with shell command examples and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write a result file when --output is used; supports mp4, avi, and mov media up to 10 MB or public media URLs.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
