## Description:

Guides ecommerce teams in generating product main-image candidates and single-variable A/B variants from approved product photos using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce merchants and creative teams use this skill to prepare platform-ready product hero images, color-SKU variants, and controlled A/B image tests from approved product photos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts are uploaded to dLazy's hosted service.

Mitigation: Use only approved commercial photos and confirm the service is trusted before uploading.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Keep keys revocable, rotate them as needed, and restrict access to local credentials.

Risk: Generated images may misrepresent product details or violate marketplace image rules.

Mitigation: Compare each image with the approved SKU and check the target platform's current requirements before publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-main-image)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image URLs]

**Output Format:** [Markdown guidance and shell commands; generated image URLs in JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses approved reference photos; produces one image per generation request and supports controlled A/B variants.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
