## Description:

A structured workflow skill dedicated to social-media carousel design using a single-confirmation, cover-first process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agent operators use this skill to plan and generate social-media carousel image sets with confirmed direction, a cover-first review loop, and consistent follow-on slides.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and referenced media may be sent to dLazy cloud services during image generation.

Mitigation: Avoid sensitive prompts or private assets unless the user accepts the disclosed cloud workflow.

Risk: The workflow requires a dLazy API key that can be stored locally or passed by environment variable.

Mitigation: Keep credentials out of prompts and shared files, and rotate or revoke keys when needed.

Risk: A global dLazy CLI install can persist tooling on the user's system.

Mitigation: Use the documented npx command when a temporary CLI invocation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [Publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables and bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces slide plans, confirmation prompts, image-generation commands, generated image URLs, and rework guidance.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
