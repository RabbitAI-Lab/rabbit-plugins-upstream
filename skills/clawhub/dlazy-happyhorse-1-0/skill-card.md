## Description:

Happy Horse 1.0 video model supports text-to-video, first-frame-to-video, reference-to-video, and video editing modes, automatically routing the selected mode to the matching sub-model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Happy Horse 1.0 hosted video-generation model from an agent workflow. It supports prompt-based generation, first-frame or reference-image guided generation, and video editing through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a locally stored dLazy API key and the security evidence says the storage should be reviewed before installation.

Mitigation: Prefer passing DLAZY_API_KEY per run, or verify permissions on ~/.dlazy/config.json before storing a persistent key.

Risk: Prompts, parameters, and referenced local media files may be sent to dLazy hosted API and media storage endpoints.

Mitigation: Only submit prompts and media files intended for processing by dLazy's hosted service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-happyhorse-1-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers or hosted media output URLs from the dLazy service.]

## Skill Version(s):

1.3.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
