## Description:

Generates 10–300-second original music from natural-language prompts using ElevenLabs music_v1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate background music and soundtracks for advertisements and short videos from text prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided files are sent to dLazy's hosted service.

Mitigation: Send only content approved for third-party processing.

Risk: A dLazy API key is stored locally for authenticated requests.

Mitigation: Protect the local key and rotate or revoke it if exposed.

Risk: The documentation's music output example shows an image/png asset.

Mitigation: Check actual CLI output with help or --dry-run before relying on automation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [dLazy CLI repository (release metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text instructions and JSON CLI response with a generated asset URL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async requests may return a task ID instead of an immediate asset URL.]

## Skill Version(s):

1.3.23 (source: server release; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
