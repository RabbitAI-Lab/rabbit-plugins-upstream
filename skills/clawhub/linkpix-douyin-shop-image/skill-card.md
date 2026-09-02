## Description:

Helps Douyin Shop merchants, short-video operators, and live-commerce teams use Qinghu qhkit to generate product hero images, carousel sets, detail images, covers, livestream stickers, and promotional campaign images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and agent users use this skill to prepare Douyin-focused product visuals and related qhkit image-generation commands. The skill guides setup, option lookup, cost estimation, token configuration, image upload handling, and delivery of generated image links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the third-party Node-based qhkit CLI.

Mitigation: Install only when the user accepts the Qinghu/qhkit dependency and review the package source and permissions before deployment.

Risk: The skill requires a Qinghu API token for authenticated generation.

Mitigation: Avoid exposing long-lived secrets, prefer environment or CLI configuration over casual sharing, and rotate or revoke the token if it is exposed.

Risk: Referenced product images may be uploaded to the Qinghu service for generation.

Mitigation: Use only images and product materials that are approved for processing by the third-party service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-douyin-shop-image)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands, JSON command payloads, configuration steps, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit option, estimate, generate, status, and configuration commands; generated images are returned as service URLs.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
