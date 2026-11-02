## Description:

Turns clothing flat-lay images and pose references into on-model e-commerce try-on images while aiming to preserve garment details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and e-commerce teams use this skill to create on-model product photography from clothing flat-lay images and pose or model references for catalog and marketing content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image inputs, including face references, leave the device; provider-uploaded media may receive public URLs.

Mitigation: Only upload images you have permission to share, avoid sensitive face references, and review the provider’s privacy terms.

Risk: Paid generation costs and estimates can vary across providers.

Mitigation: Set the provider explicitly and inspect the dry run and cost estimate before paid generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/flat-lay)
- [dLazy CLI local files and data URLs](https://github.com/dlazy-ai/cli#local-files--data-urls)

## Skill Output:

**Output Type(s):** [Images, Shell commands, Guidance]

**Output Format:** [Generated image files (JPEG, PNG, or WebP) with shell commands and instructions for image generation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses garment and pose or model reference images; generated visual fidelity can vary.]

## Skill Version(s):

1.0.25 (source: frontmatter; server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
