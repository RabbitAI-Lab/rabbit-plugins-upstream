## Description:

Qinghu AI Image Watermark Removal helps agents use LinkPix through qhkit to remove watermarks, logos, or text from a single image and return the processed result.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content teams use this skill to ask an agent to remove watermarks, logos, or visible text from authorized image assets through the Qinghu/LinkPix workflow. The skill is most relevant for ecommerce images, social media graphics, and similar image cleanup tasks where the user can confirm rights and credit spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade an unpinned third-party qhkit CLI before running the workflow.

Mitigation: Use an isolated, unprivileged, pinned qhkit installation where possible and avoid sudo or broad global upgrades.

Risk: Input images are uploaded to an external service and workflow runs may spend Qinghu credits.

Mitigation: Submit only images the user owns or is authorized to process, run an estimate first, and wait for user confirmation before generation.

Risk: Watermark or logo removal can be misused on copyrighted or third-party assets.

Mitigation: Remind users to process only authorized material and avoid using removed-watermark outputs in ways that violate rights or platform rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-watermark-remove)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Submits one image per workflow job and reports qhkit status, result image URLs, and final Qinghu credit usage when complete.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
