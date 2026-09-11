## Description:

This skill guides agents to batch translate text in ecommerce product images into target languages with qhkit while preserving the original layout and design style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External cross-border ecommerce sellers and operators use this skill to localize product main images and detail images by translating embedded text while keeping the visual layout similar. Agents use it to prepare qhkit image-generation commands, estimate credits, handle setup, and return generated image URLs with review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade an unpinned third-party qhkit CLI package that handles local images and an API token.

Mitigation: Use the skill only when the qhkit package and Qinghu service are trusted; prefer a pinned, reviewed package version, an isolated install, and explicit approval before upgrades or registry mirror use.

Risk: Images and API tokens may be processed by the third-party Qinghu service through qhkit.

Mitigation: Avoid sending sensitive images unless the service is approved for that data, keep API tokens in approved secret storage, and review qhkit configuration before use.

Risk: Generated image translations can contain incorrect text, altered numbers, or small visual changes because the workflow uses generative redrawing rather than pixel-level text replacement.

Mitigation: Manually inspect each output for spelling, brand names, prices, specifications, logos, and product structure; explicitly instruct the model to preserve numbers when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-translate)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated image URLs, credit estimates, setup steps, and manual review notes for translated image text.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
