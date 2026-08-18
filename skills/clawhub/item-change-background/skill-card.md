## Description:

Helps agents replace plain product-image backgrounds with photorealistic scenes while preserving the item and prompting for grounded shadows, reflections, and matching light.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce teams, and developers use this skill to turn white-background product photos into lifestyle scene images through dLazy's hosted image-editing workflow. It guides image input checks, prompt construction, CLI commands, and quality review for text-described backgrounds or uploaded background images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to dLazy's hosted service for inference.

Mitigation: Avoid submitting confidential product imagery unless dLazy's terms, access controls, and data handling meet the user's use case.

Risk: Generated files may be stored on dLazy-hosted URLs.

Mitigation: Review output sharing and retention expectations before using sensitive assets or unreleased product imagery.

Risk: The dLazy CLI stores an organization API key locally after login or manual authentication.

Mitigation: Use the pinned CLI version, protect the local config, and rotate or revoke the organization key when access changes.

Risk: Generated lifestyle scenes can imply unsupported product properties or unsuitable use contexts.

Mitigation: Review generated images for product fidelity, realistic placement, and consistency with approved product claims before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/item-change-background)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local image files when commands are run with --save and hosted output URLs from dLazy.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
