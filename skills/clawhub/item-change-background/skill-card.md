## Description:

Turns product photos on plain backgrounds into photorealistic lifestyle scenes with matching lighting and grounded shadows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and creative teams use this skill to place product photos into realistic scenes while preserving product details and matching shadows, reflections, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images and prompts are sent to the configured cloud image provider.

Mitigation: Inspect requests with --dry-run, choose an explicit provider and save path, and avoid confidential images when third-party processing is not allowed.

Risk: Provider API credentials may remain valid after access changes.

Mitigation: Rotate or revoke API keys when access changes.

Risk: Generated scenes may alter product details or produce mismatched lighting and shadows.

Mitigation: Review generated images for product fidelity, grounded contact shadows, consistent lighting, and clean edges before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [Provider CLI guide](references/provider-cli.md)
- [Image model options](references/model-flags.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands and image-editing prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configured image providers generate scene images that can be saved locally.]

## Skill Version(s):

1.0.14 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
