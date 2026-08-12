## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to provide reference audio and a prompt so an agent can call dLazy's hosted Vidu Audio Clone service to generate new speech audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can be used on voices the user is not authorized to clone.

Mitigation: Require explicit confirmation that the user has rights and consent before uploading reference audio or generating cloned speech.

Risk: The skill sends prompts and selected audio files to dLazy's hosted API and media storage.

Mitigation: Confirm uploads with the user, avoid sensitive audio, and use dry-run mode when checking payloads or costs.

Risk: The skill stores a dLazy API key in local CLI configuration or can read DLAZY_API_KEY from the environment.

Mitigation: Use OS-user-restricted config permissions, rotate or revoke keys when needed, and avoid exposing keys in logs or shared shell history.

Risk: Generation calls may incur service costs or fail because of insufficient balance.

Mitigation: Use cost estimates where appropriate and require confirmation before paid generation calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return asynchronous task identifiers or hosted media URLs from files.dlazy.com.]

## Skill Version(s):

1.3.7 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
