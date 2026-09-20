## Description:

AI-powered pet sleep quality analysis from a fixed bed/rest-area camera that distinguishes sleeping from awake states, accumulates sleep duration, counts roll-overs and startle-awakenings, and returns a 0-100 sleep-quality score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze pet rest-area video for sleep duration, roll-over count, startle-awakening frequency, and a structured sleep-quality report. The result is intended as visual sleep-health guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet rest-area videos and report-history requests are sent to the publisher's cloud service.

Mitigation: Use only with explicit consent for video upload and history access, and avoid submitting sensitive footage unless the data flow is documented and accepted.

Risk: Security evidence reports automatic identity creation or reuse and local token persistence.

Mitigation: Require secure, scoped credential handling and clear user/account separation before deployment.

Risk: Security evidence reports cleartext development endpoint configuration.

Mitigation: Confirm development HTTP endpoints are removed and production HTTPS endpoints are used before installation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Pet Sleep Quality Analysis API Documentation](artifact/references/api_doc.md)
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report text or JSON analysis output with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save the analysis output to a file when an output path is provided.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
