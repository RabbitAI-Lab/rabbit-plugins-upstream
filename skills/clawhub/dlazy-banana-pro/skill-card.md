## Description:

Generate/edit images with Nano Banana Pro, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy Nano Banana Pro CLI from prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local files may be sent to dLazy services for image generation.

Mitigation: Avoid passing private files or sensitive prompts unless the user is comfortable sending them to dLazy.

Risk: Using the skill may install or run a third-party npm CLI package.

Mitigation: Review the referenced CLI package before use, or run the pinned package with npx to avoid keeping a persistent global binary.

Risk: The skill requires a dLazy API key stored in local CLI configuration or supplied through an environment variable.

Mitigation: Use scoped keys, rotate or revoke keys when needed, and avoid exposing API keys in prompts, logs, or shared shell history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI returns generated image URLs and can save result assets when requested.]

## Skill Version(s):

1.2.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
