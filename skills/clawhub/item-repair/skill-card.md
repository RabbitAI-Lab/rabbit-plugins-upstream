## Description:

Helps retouch product photos for listings by reducing incidental wrinkles, correcting layout and lighting, and cleaning backgrounds while preserving product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and creative teams use the skill to prepare product photos for listings, removing incidental wrinkles and distractions without changing the product's design or concealing defects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos and prompts may be sent to the selected cloud image provider.

Mitigation: Use --dry-run to review requests and send private images only when the provider's handling is acceptable.

Risk: Broad retouching requests may trigger an unwanted image-editing call.

Mitigation: Confirm ambiguous requests before invoking the skill.

Risk: Retouching may inadvertently alter structural details or hide product defects.

Mitigation: Require preservation of design and genuine defects, then compare edited images against the originals.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/item-repair)
- [Provider setup and output reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Image files, Shell commands, Guidance]

**Output Format:** [JPEG product images with text instructions and optional JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one to four views of the same product; compare results with originals before publication.]

## Skill Version(s):

1.0.18 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
