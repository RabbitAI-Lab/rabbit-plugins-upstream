## Description:

Generates realistic digital human broadcast videos from portrait images and audio or text using Jimeng OmniHuman 1.5.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate digital-human broadcast videos through the dLazy hosted API, supplying a portrait image plus audio or text and receiving hosted result URLs or saved media files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts, parameters, and selected image or audio files to the dLazy hosted API and media storage.

Mitigation: Review the data before use and avoid submitting sensitive media or prompts unless the dLazy service terms and data handling are acceptable.

Risk: Authentication uses a dLazy API key that can be stored in the local CLI config.

Mitigation: Use per-invocation DLAZY_API_KEY for sessions where persistent local credential storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill installs or invokes an external pinned npm CLI package.

Mitigation: Review the @dlazy/cli package and source before installation, and prefer the pinned version declared by the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-omnihuman-1-5)
- [dlazyai publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON response payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media URLs may be returned directly or downloaded with --save; --no-wait returns an async task ID for polling.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
