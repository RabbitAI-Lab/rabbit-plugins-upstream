## Description:

ElevenLabs music_v1 generates 10-300 second original music from natural-language prompts for BGM, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to ask an agent to generate short original music through the dLazy CLI and hosted API. It supports background music, advertising tracks, and short-video soundtracks from prompt, duration, and output-saving options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party CLI and hosted API that receive prompts, parameters, and referenced media files.

Mitigation: Review the linked dLazy CLI source/package and avoid sending sensitive prompts or files unless the user accepts the third-party service exposure.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: A global npm install persists third-party executable code on the machine.

Mitigation: Use the pinned npx invocation when a non-persistent execution path is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted output URLs, async task identifiers, or local saved files when --save is used.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
