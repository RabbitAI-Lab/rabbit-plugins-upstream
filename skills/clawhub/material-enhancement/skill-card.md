## Description:

Enhances clothing material texture and reconstructs fabric detail in a blurred commerce image by using a high-resolution product image as the fabric reference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce content teams use this skill to produce prompts and image-generation commands that improve garment fabric texture while preserving the model, pose, background, color, framing, and garment silhouette.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and source images may be sent to the selected cloud provider during generation.

Mitigation: Use the skill only with images and prompts that are approved for the configured provider, and review provider data handling before execution.

Risk: Remote image URLs can introduce untrusted fetching behavior.

Mitigation: Prefer local image files or trusted public image hosts until URL handling has host, redirect, content-type, size, and timeout validation.

Risk: The optional npx CLI path executes external package code.

Mitigation: Use an approved local CLI installation or an internally reviewed package source in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter list](references/model-flags.md)
- [Related fabric-on-body skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/fabric-on-body/skill.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and prompt templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-editing prompts and command examples that may save generated JPEG outputs through a selected cloud provider.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
