## Description:

Translates text in e-commerce product images into target languages while aiming to preserve their layout and design through image regeneration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Cross-border sellers and their agents use this skill to localize product listing and detail images for different languages, including batch image translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating a third-party CLI may introduce unreviewed changes.

Mitigation: Review or pin the qhkit version before installation when possible.

Risk: Product images are sent to the Qinghu service and an access token is required.

Mitigation: Share only images appropriate for that service and protect the token as a credential.

Risk: Generated images may alter text, prices, logos, or product details.

Mitigation: Check each translated image against its source before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-image-translate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Image URLs]

**Output Format:** [Markdown with links to translated images and credit usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch results can be matched to source filenames.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
