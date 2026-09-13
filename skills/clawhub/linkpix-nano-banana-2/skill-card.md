## Description:

Helps ecommerce operators, ad designers, and sellers use LinkPix/qhkit image generation workflows to create and iterate product images, advertising creatives, covers, backgrounds, and image edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce teams, marketplace sellers, and creative operators use this skill to select qhkit image models, prepare prompts and reference images, estimate credits, and generate commercial product imagery for channels such as Taobao, JD, Pinduoduo, Amazon, and TikTok Shop.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can involve external image upload and credit-consuming generation.

Mitigation: Confirm model, image count, size, quality, reference images, and estimated credits with the user before running generation commands.

Risk: The skill may prompt for API key setup.

Mitigation: Do not ask users to paste API keys into chat; have them configure QHKIT_TOKEN or local qhkit credentials through a secure terminal or secret manager.

Risk: The skill includes installation or upgrade flows for command-line tooling.

Mitigation: Prefer pinned local installs, avoid unreviewed global latest upgrades, and require explicit user approval for package installation or upgrade.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-nano-banana-2)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command parameters, credit estimates, operational warnings, and generated image URLs when executed by an agent.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
