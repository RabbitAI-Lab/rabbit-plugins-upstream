## Description:

Generates a cohesive e-commerce product image set from one reference image, keeping the same product or outfit consistent across hero, lifestyle, detail, comparison, and alternate-pose shots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce sellers, designers, and agent operators use this skill to turn one product or outfit image into a multi-shot listing set for marketplace main images and detail pages. It is useful when a catalog needs consistent multi-angle, lifestyle, macro, comparison, or pose variants from limited source photography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-provided product images and prompts are sent to dLazy's cloud service, and generated outputs are hosted by dLazy.

Mitigation: Use only images and prompts that are appropriate for third-party cloud processing, and review dLazy's service terms for data handling and retention requirements.

Risk: The dLazy CLI requires an API key that may be saved locally.

Mitigation: Prefer per-invocation environment variables or npx when appropriate, protect local CLI configuration files, and rotate or revoke keys from the dLazy dashboard when access changes.

Risk: Generated product images may drift from the reference item or imply unsupported product details.

Mitigation: Review the full output set before publication and rerun any image that changes product shape, color, material, structure, claims, text, or watermark status.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fission-pattern)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline bash commands and generated image file or URL outputs from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-supplied reference image, product name, and selling points to produce prompt variants and CLI calls for a coherent image set.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
