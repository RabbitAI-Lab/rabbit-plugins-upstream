## Description:

This skill analyzes gecko and lizard tail images, videos, or URLs to detect abnormal tail shortening, tail-tip wounds, scabs, and possible tail-loss events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External reptile keepers, breeders, and developers use this skill to analyze enclosure camera images, videos, or submitted media URLs for tail-loss signals, produce structured event reports, and review cloud-stored historical tail-loss records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted enclosure images, videos, or media URLs may be sent to a vendor cloud service.

Mitigation: Use only media you intend to share with the vendor service, and avoid private or signed URLs unless sharing them is acceptable.

Risk: The skill may automatically create or reuse an internal identity and store returned session tokens in the workspace data directory.

Mitigation: Review workspace data retention and token-handling practices before deployment, and clear stored tokens according to local policy when access is no longer needed.

Risk: Cloud history queries and limited user control over uploads may expose data beyond the local agent session.

Mitigation: Confirm the cloud-backed workflow is acceptable for the deployment environment and inform users before processing sensitive reptile enclosure media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-reptile-tail-loss-detection-analysis)
- [API interface documentation](artifact/references/api_doc.md)
- [Smyx Analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis reports with visual findings, alert levels, recommended actions, disclaimers, and optional report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video files or media URLs and can write results to an output file; history queries return Markdown tables from the cloud API.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
