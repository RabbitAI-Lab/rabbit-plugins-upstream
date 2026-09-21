## Description:

A comprehensive generation skill that routes image, video, and audio generation requests to the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to ask an agent for image, video, or audio generation while the skill selects an appropriate dLazy CLI subcommand and parameters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media files may be sent to the dLazy hosted API and media storage.

Mitigation: Use the skill only for content that is appropriate to process through dLazy's hosted service, and avoid submitting sensitive media unless that use is approved.

Risk: Generated outputs are hosted remotely and returned as service URLs.

Mitigation: Review generated output URLs and sharing expectations before using them in downstream workflows or public materials.

Risk: Using dlazy login or dlazy auth set can persist an API key on disk.

Mitigation: For tighter credential control, use the documented npx invocation and provide DLAZY_API_KEY per run instead of a global install and saved login.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands and dLazy CLI JSON envelopes or hosted output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce remotely hosted image, video, audio, SVG, or mask outputs through files.dlazy.com.]

## Skill Version(s):

1.3.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
