## Description:

ElevenLabs music_v1 generates 10-300 second original music from a natural-language prompt for background music, ads, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate original music from text prompts through the dLazy ElevenLabs Music command, including background music, advertising tracks, and short-video soundtracks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and parameters to dLazy's hosted API and may upload local file paths passed to media fields.

Mitigation: Review inputs before invocation, avoid sending sensitive content, and use only intended local files.

Risk: The CLI can store an API key in ~/.dlazy/config.json during login or manual authentication.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when persistent local storage is not desired, and rotate or revoke keys as needed.

Risk: The artifact includes documentation mistakes in the output example and unrelated image/video error text.

Mitigation: Treat the scanner guidance as authoritative and have the publisher correct the example before relying on it for integration tests.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return asynchronous task identifiers; generated asset URLs are hosted on files.dlazy.com and --save can download results locally.]

## Skill Version(s):

1.3.17 (source: server release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
