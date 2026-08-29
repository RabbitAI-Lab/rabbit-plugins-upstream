## Description:

多单品搭配融图 Image Fusion helps ecommerce teams combine up to eight product images into one modeled outfit image while preserving each item's visible details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, content teams, and developers use this skill to turn multiple catalog product photos into a complete styled look image for storefront, listing, or campaign workflows. It guides the agent to map each reference image to a specific worn item, choose generation parameters, and save generated image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, model references, and prompts may be sent to the selected cloud image provider.

Mitigation: Use dry-run or doctor mode first, choose the provider deliberately, and avoid confidential assets or internal-only URLs.

Risk: Fixed model traits or reference faces can create unwanted demographic assumptions or likeness concerns.

Mitigation: Use user-selected or neutral model traits, only use model references with appropriate rights, and avoid forged endorsement scenarios.

Risk: Generated outfit images can omit an item, mix colors, mis-layer garments, or move distinctive patterns.

Mitigation: Map each image to a specific wearing position, state layer order explicitly, generate batches for selection, and run visual quality checks before publishing.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/image-fusion)
- [seedream-5.0 parameter reference](references/model-flags.md)
- [Provider CLI reference](references/provider-cli.md)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with bash command examples, prompt templates, and generated image file paths when saved]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run checks, provider selection, optional brand configuration, batch generation, and local image output writes.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
