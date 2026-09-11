## Description:

Replaces the fabric on a garment style reference using a fabric swatch, preserving the original cut, construction, camera angle, and layout while generating a visual preview of the new material.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce operators, and apparel teams use this skill to generate fabric-on-garment visual previews before physical sampling. It is intended for comparing material options while keeping garment geometry and construction stable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Garment images, fabric swatches, prompts, and provider credentials may be sent to the selected cloud image-generation provider.

Mitigation: Use only trusted provider configurations and avoid running the skill with sensitive images or credentials unless the provider's data handling is acceptable.

Risk: An optional Ark provider path can use ARK_BASE_URL to send API keys and private images to an arbitrary endpoint.

Mitigation: Do not set ARK_BASE_URL unless the endpoint has been reviewed and is fully trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/fabric-on-body)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 model flags](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with bash commands and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated outputs are visual previews, typically saved as JPEG image files; they do not represent physical fabric hand feel or weight.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
