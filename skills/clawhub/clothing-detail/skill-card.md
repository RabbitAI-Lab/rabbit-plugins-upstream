## Description:

服装工艺细节放大图。服装图 -> 面料纹理、走线、织法的微距特写。当用户说「细节图」「特写」「面料放大」「工艺展示」「近景细节」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers, marketers, and catalog operators use this skill to turn garment product images into macro detail shots for collars, cuffs, hems, buttons, zippers, embroidery, prints, stitch structure, and fabric fibers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper scripts can upload arbitrary local files or fetch arbitrary URLs when those values are supplied as image inputs.

Mitigation: Use only trusted image paths and trusted image URLs, prefer local garment files inside the active workspace, and do not allow untrusted page content or automation to choose --images, --brand, or --save arguments.

Risk: Provider credentials and uploaded images may be sent to dLazy or another configured image provider.

Mitigation: Review the selected provider before execution, run dry runs first when possible, and use only credentials and images approved for that provider's data handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/clothing-detail)
- [Provider CLI reference](references/provider-cli.md)
- [gpt-image-2 parameter reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates and bash command examples for generating saved JPEG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image files are commonly saved as JPEG outputs, with 1024x1024 or 1024x1536 dimensions and high quality settings when commands are executed.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
