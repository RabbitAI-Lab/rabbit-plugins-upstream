## Description:

Turns flat-lay garment photos into 3D ghost-mannequin product images while preserving garment details such as color, texture, prints, ribbing, and labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators, designers, and agents use this skill to convert compliant flat-lay garment images into more dimensional product visuals without using a human model. It supports garment-type, shape-reference, prompt, material-enhancement, and aspect-ratio controls for product imagery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected garment images and prompts are sent to dLazy's hosted service, and generated outputs are hosted by dLazy.

Mitigation: Use only images and prompts appropriate for third-party cloud processing, and review dLazy service terms before use.

Risk: The dLazy API key may be stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use the pinned CLI or npx path, restrict local credential access, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: Generated product images can alter garment shape or introduce a mannequin, body, or incorrect texture if inputs or prompts are weak.

Mitigation: Inspect outputs before publication, use clear single-garment flat-lay inputs, include explicit no-person/no-mannequin prompt constraints, and rerun with higher quality when texture fidelity matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/to-3d)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazyai/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped CLI responses; generated assets are returned as hosted URLs or saved image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports one flat-lay garment image, an optional shape reference image, prompt controls, 1:1 or 3:4 generation sizes, JPEG output, and batch generation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
