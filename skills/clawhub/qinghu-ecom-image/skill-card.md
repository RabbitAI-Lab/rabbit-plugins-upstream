## Description:

This skill helps agents route and generate ecommerce product images, image sets, detail-page graphics, white-background images, and campaign visuals through Qinghu AI's qhkit CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Agents assisting ecommerce sellers and marketers use this skill to choose the right Qinghu AI image-generation mode, prepare qhkit commands, estimate credits, and return generated product image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable third-party CLI installation and upgrade instructions can give unreviewed qhkit code broad execution authority.

Mitigation: Install only trusted, reviewed qhkit versions; prefer pinned versions and avoid executing upgrade commands copied from CLI messages without review.

Risk: The skill requires an API token and uploads product images to the Qinghu service.

Mitigation: Protect the token, use a constrained environment, and upload only product images approved for the provider's service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-ecom-image)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs and actual credit usage returned by qhkit.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
