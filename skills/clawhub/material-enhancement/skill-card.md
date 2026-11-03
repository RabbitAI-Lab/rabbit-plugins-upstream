## Description:

Enhances clothing photos by rebuilding fabric texture and fine detail from a high-resolution product reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce image creators use the skill to improve fabric texture in a clothing photo with a high-resolution reference of the same item, while aiming to preserve the garment and surrounding scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and prompts are sent to the selected cloud provider, whose handling and retention practices may vary.

Mitigation: Choose the provider explicitly, use --dry-run to review the request, and check its retention terms before sending sensitive images.

Risk: A product reference for a different item can produce inaccurate fabric details.

Mitigation: Confirm both images show the same product and save the enhanced result separately to preserve the original.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](artifact/references/provider-cli.md)
- [gpt-image-2 model flags](artifact/references/model-flags.md)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Files]

**Output Format:** [Enhanced image files, JPEG by default]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Saved to a user-selected path; image size can be chosen to match the source aspect ratio.]

## Skill Version(s):

1.0.28 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
