## Description:

材质质感增强与纹理重建。糊掉的图 + 高清商品图 -> 纹理清晰可信的图。当用户说「增强质感」「图糊了」「补纹理」「提清晰度」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and catalog-production teams use this skill to improve garment material fidelity in product images while preserving the model, pose, framing, background, color, and garment silhouette. It guides an agent through prompt construction, image-input checks, provider configuration, and output review for cloud image-editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner verdict is suspicious because the bundled helper code is broader than the advertised material-enhancement purpose.

Mitigation: Review the bundled helper scripts before deployment and keep use to the documented material-enhancement command path.

Risk: The workflow may upload prompts and product or model images to configured cloud providers.

Mitigation: Use approved provider credentials, avoid sensitive or untrusted image inputs, and review output paths before execution.

Risk: Material enhancement can transfer the wrong texture or alter unintended image regions when inputs are mismatched or prompts are underspecified.

Mitigation: Confirm the reference and source images are the same product, lock non-garment regions in the prompt, and compare outputs for face, background, color, and silhouette preservation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/material-enhancement)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline bash commands and parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces prompts, command examples, provider setup guidance, and review criteria; generated image files are saved by the configured image provider workflow.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
