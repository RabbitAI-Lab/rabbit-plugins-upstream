## Description:

通过 qhkit CLI（npm @iqinghu/qhkit）AI 自动优化商品主图的构图、光影、质感及细节，提升商品吸引力与点击率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace users and commerce operators use this skill to guide an agent through optimizing product main images with LinkPix/qhkit, including scene generation, targeted quality improvements, and multi-image redesigns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload selected product images to third-party LinkPix/qhkit services.

Mitigation: Require explicit user approval before uploading local image files or running generation commands.

Risk: Generation commands may spend service credits.

Mitigation: Estimate credits before generation when reporting costs, and confirm the user wants to proceed when credit usage is material.

Risk: The skill may install or update a third-party Node CLI and bootstrap Node when missing.

Mitigation: Require approval before package installation, Node bootstrapping, or CLI upgrades, and report installation failures clearly.

Risk: API tokens may be exposed if pasted into chat or inline shell commands on shared machines.

Mitigation: Use protected configuration files or environment secrets instead of inline tokens.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-main-image-optimize)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides image generation workflows that return image URLs and credit usage through the qhkit CLI.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
