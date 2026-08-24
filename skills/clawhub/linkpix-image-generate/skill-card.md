## Description:

Generates commercial ecommerce images from text prompts or optional reference images with LinkPix/qhkit, and can polish product prompts before generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, ecommerce operators, and developers use this skill to generate product or scene images from prompts, optionally guided by uploaded product or reference images. It also helps refine weak product prompts before submitting a paid generation task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require API token configuration and asks agents to handle credentials directly.

Mitigation: Prefer a platform-managed qhkit configuration when available; otherwise configure credentials outside chat or provide only the minimum token needed.

Risk: Prompts and selected reference images may be uploaded to the LinkPix/qhkit service.

Mitigation: Use the skill only with prompts and images acceptable for that service, and confirm privacy or data-use requirements before uploading sensitive material.

Risk: Image generation creates a task and can consume credits.

Mitigation: Run the estimate action first, disclose the expected credit cost and key parameters, and wait for explicit user approval before generation.

Risk: The skill can request broad persistent environment changes such as global npm installs or PATH updates.

Mitigation: Prefer an existing managed qhkit install; when installation is necessary, keep changes scoped and review the package and command before applying persistent environment changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-image-generate)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup tutorial](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce qhkit command plans, cost estimates, prompt-polishing text, and final image URLs returned by the service.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
