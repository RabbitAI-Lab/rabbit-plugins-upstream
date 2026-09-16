## Description:

Generates and edits images by selecting an appropriate dLazy CLI image model from the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users invoke this skill to generate, edit, upscale, segment, vectorize, or otherwise process images through dLazy-hosted models from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-supplied media may be sent to dLazy-hosted API and file services.

Mitigation: Use the skill only with content approved for transfer to dLazy, and avoid sensitive or regulated inputs unless the service terms and data-handling requirements have been reviewed.

Risk: The skill can use a third-party npm CLI with stored dLazy credentials and paid credits.

Mitigation: Prefer npx or another non-global execution path when possible, review the package or source before use, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: The artifact describes broader media commands than the image-only purpose implies.

Mitigation: Keep use scoped to image generation and image-processing tasks, and inspect the selected dLazy subcommand help before execution.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted result URLs from files.dlazy.com through the dLazy CLI.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
