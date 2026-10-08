## Description:

Identifies previously enrolled acquaintances in images or videos through face comparison and provides recognition reports for home or office monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home and office users can compare images or videos against an enrolled face database to identify familiar people and review past recognition reports. Results are advisory and are not suitable for legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face-containing images or videos, potentially including home or office surveillance footage, are sent to a cloud service.

Mitigation: Use only with appropriate consent and review the service's account and data-retention expectations before uploading sensitive media.

Risk: The skill can silently create or reuse a local identity, associate reports with it, and store account tokens in a workspace SQLite database.

Mitigation: Review account association and protect access to the workspace database and stored tokens before using the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-familiar-person-recognition-analysis)
- [Recognition API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured recognition results and report links; Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file.]

## Skill Version(s):

1.0.17 (source: server-resolved release; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
