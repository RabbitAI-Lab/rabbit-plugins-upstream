## Description:

Through fixed enclosure cameras, the skill periodically captures tail images of geckos and lizards and uses AI visual analysis to detect tail length changes, tail-tip wounds, scabs, or abnormal shortening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, vivarium operators, breeders, and developers use this skill to analyze reptile tail images or videos, compare tail length against history or body-length references, and produce structured tail-loss event reports with suggested next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reptile enclosure media, remote URLs, account identifiers, or historical report metadata may be sent to the publisher's services.

Mitigation: Install only if this data sharing is acceptable, and prefer a version that asks for explicit confirmation before uploads or history queries.

Risk: The skill silently creates or reuses an account identity and stores tokens locally.

Mitigation: Review local token handling and retention before deployment, and require documented deletion and retention controls for production use.

Risk: Automatic cloud history queries may expose report metadata without clear user control.

Mitigation: Limit use to environments where automatic account linkage and cloud history access are approved, or require an updated workflow with explicit user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and command-line output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and structured tail measurement, morphology, alert level, recommended action, and disclaimer fields.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
