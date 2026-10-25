## Description:

Identifies cat and dog breeds and distinguishes individual pets in images or videos, including multi-pet households.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use the skill to identify cats and dogs in images or videos, distinguish pets in multi-pet households, and view past analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos are uploaded to external analysis services.

Mitigation: Obtain consent before uploading pet media and confirm that the external services meet applicable privacy requirements.

Risk: The skill automatically creates and reuses a persistent identity and local token store.

Mitigation: Review identity and token persistence before installation; avoid use where silent identity creation is unacceptable.

Risk: Report history remains available through the cloud service, while retention and deletion controls are unclear.

Mitigation: Confirm report and metadata retention and deletion controls with the service provider before using sensitive media.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [Pet analysis API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured pet analysis report or Markdown report-history table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include breed predictions, individual distinctions, confidence values, and report links; results are not a substitute for professional breed verification.]

## Skill Version(s):

1.0.15 (source: server-resolved ClawHub release; bundled skill frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
