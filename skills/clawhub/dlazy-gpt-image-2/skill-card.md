## Description:

GPT Image 2 model for text-to-image and image editing, including generation from text and editing or synthesis with reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy GPT Image 2 CLI for text-to-image generation and reference-image editing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced local media may be sent to the dLazy hosted API and media storage.

Mitigation: Only submit prompts and files that are acceptable to upload to a third-party hosted service.

Risk: The skill uses a third-party npm CLI and requires a dLazy API key.

Mitigation: Prefer npx or the DLAZY_API_KEY environment variable when avoiding persistent global installs or saved credentials, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses containing generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can save generated assets locally with --save or return asynchronous task identifiers with --no-wait.]

## Skill Version(s):

1.3.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
