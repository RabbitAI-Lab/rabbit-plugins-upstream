## Description:

智能识别商品主体，一键替换图片背景，生成不同风格的营销场景图，无需 PS。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate ecommerce product images with replacement backgrounds or synthesized marketing scenes while preserving the product subject.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or auto-upgrade an unpinned global third-party qhkit CLI.

Mitigation: Confirm trust in @iqinghu/qhkit before installation, prefer a pinned local install or sandboxed account where available, and review upgrade commands before running them.

Risk: The workflow can upload product images to the LinkPix/qhkit service, configure an API token, and incur credit charges.

Mitigation: Use approved images and accounts, protect API tokens, and run the estimate command before generation when users need cost confirmation.

Risk: Generated background replacement can slightly change product details such as text, logos, or structure.

Mitigation: Review generated images for product accuracy before publication or customer-facing use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-background-swap)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to call qhkit image generation commands that return image URLs, credit usage, and JSON status messages.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
