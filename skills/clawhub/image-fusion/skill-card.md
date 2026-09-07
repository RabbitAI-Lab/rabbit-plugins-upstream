## Description:

Helps agents generate e-commerce outfit images by combining up to eight product photos into one complete look on a single model while preserving each item's appearance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, merchandisers, and creative operators use this skill to turn multiple apparel or accessory product photos into a unified commercial look image. It guides prompt construction, reference-image ordering, dry runs, generation commands, and output quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and input images may be sent to cloud image-generation providers.

Mitigation: Install and run the skill only when the user accepts that data flow; avoid confidential or sensitive imagery unless the selected provider is approved.

Risk: The helper scripts can fetch reference images from network URLs.

Mitigation: Prefer local image files or trusted public image URLs, and avoid untrusted URLs.

Risk: Credentials may be forwarded to a custom Ark API endpoint if ARK_BASE_URL is set.

Mitigation: Set ARK_BASE_URL only for endpoints the user fully trusts to receive the Ark API key.

Risk: The bundled task set includes a remove-watermark capability that may be misused on third-party content.

Mitigation: Do not use remove-watermark behavior on content unless the user has the rights and authorization to modify it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/image-fusion)
- [seedream-5.0 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance with CLI commands; generated assets are saved as image files at the requested path.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to eight product item images plus optional pose or model references; default image-fusion generation uses 3:4 at 2K.]

## Skill Version(s):

1.0.6 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
