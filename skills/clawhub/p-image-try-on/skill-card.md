## Description:

Use when someone wants virtual try-on: dress a person in clothes from reference photos for fashion or ecommerce.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate virtual try-on images for fashion or ecommerce by applying reference garments to a provided person image through Pruna.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads person and garment images to Pruna-hosted endpoints, which may involve personal photos or sensitive visual data.

Mitigation: Use only images the user has rights and consent to process, avoid sensitive or minor images unless safeguards are in place, and review Pruna privacy and retention terms before use.

Risk: Installing the full Pruna skill suite expands the trusted dependency surface beyond this try-on workflow.

Mitigation: Install only the Pruna dependency skills needed for this workflow unless the broader package set has been reviewed and trusted.

Risk: Ambiguous garment references or prompts can cause the output to alter the intended person, garment, or pose.

Mitigation: Confirm person_image, garment_images, optional prompt, and optional reference_pose before paid generation; use the prompt only to disambiguate supplied references.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/p-image-try-on)
- [Editorial seated and artistic shirt reference output](https://replicate.com/p/p47vaj1f91rmw0cyt4er0z2zd4)
- [Complex collaged suit reference output](https://replicate.com/p/tf7gqansnnrmt0cyt4j8mpx1c8)
- [Mirror selfie and cap reference output](https://replicate.com/p/hp60wyj355rmy0cyt4psnc2mh0)
- [Multi-garment streetwear stack reference output](https://replicate.com/p/bak21xr79srmr0cyt52tap1nw8)
- [Pleated blouse golden-hour reference output](https://replicate.com/p/g9hd22x26drmr0cytmtsx11c5g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with curl commands and JSON request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires PRUNA_API_KEY plus user-provided person and garment image URLs.]

## Skill Version(s):

1.0.11 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
