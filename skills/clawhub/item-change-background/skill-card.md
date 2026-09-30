## Description:

Turns product photos on plain backgrounds into realistic lifestyle scenes with matched lighting, reflections, and contact shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants, product photographers, and designers use this skill to place product images into plausible scenes for e-commerce visuals while preserving product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud image provider.

Mitigation: Use only images approved for cloud processing; do not submit confidential or internal image URLs.

Risk: Image-generation requests may incur charges or expose provider credentials.

Mitigation: Preview requests with dry-run before paid calls, and use scoped, revocable API keys.

Risk: Related task profiles may include watermark removal outside this skill's purpose.

Mitigation: Avoid unrelated profiles unless you have explicit rights and a legitimate need.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI reference](references/provider-cli.md)
- [Image model parameters](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [JPEG product scene images, with optional JSON results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved image paths or hosted image URLs; review product fidelity and scene realism before publication.]

## Skill Version(s):

1.0.15 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
