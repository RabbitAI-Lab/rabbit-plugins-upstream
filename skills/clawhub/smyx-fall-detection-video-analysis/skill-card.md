## Description:

Analyzes video of monitored areas for possible falls and provides structured results and historical reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and home-monitoring teams use the skill to review videos for possible falls involving people living alone and to retrieve prior analysis reports. Alerts require human confirmation before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home-monitoring videos and report queries are sent to the vendor cloud.

Mitigation: Upload only authorized footage and confirm the vendor's privacy, retention, and deletion practices before use.

Risk: The skill may create or reuse identities without prompting and stores tokens locally.

Mitigation: Ask the publisher how identities are verified, tokens are protected, and local credentials and report history can be revoked or deleted.

Risk: A fall-detection result may not reliably establish whether someone needs assistance.

Mitigation: Treat alerts as safety prompts and have a person confirm suspected falls promptly.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [Fall detection API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured text or JSON analysis results; Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include monitoring findings, recommendations, and report links; results can be saved to a file.]

## Skill Version(s):

1.0.17 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
