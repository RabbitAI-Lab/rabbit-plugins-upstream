## Description:

Using fixed-camera footage at a home entrance or kindergarten gate, this skill identifies visible crying, clinging, and resistance behaviors in children during drop-off and estimates a separation-anxiety level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and early-childhood educators can use it to review drop-off footage for visible crying, clinging, and resistance behaviors, and receive an estimated severity level and soothing suggestions. It supports observation and early awareness; it does not provide a psychological diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the no-analysis option is ineffective, so identifiable child footage may still be analyzed or uploaded.

Mitigation: Do not use identifiable child footage until a working no-analysis mode and explicit controls for analysis and uploads are verified. Obtain informed parental consent before use.

Risk: The security review reports credential handling that exposes sensitive information; child-video processing also depends on the receiving service's privacy practices.

Mitigation: Protect credentials in secure storage, keep them separate from identity fields, disable sensitive HTTP logging, and review the service's retention and deletion terms before uploading footage.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior analysis reports and Markdown history tables with metrics, an estimated level, alerts, and suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize visible behavior and may include links to historical records.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
