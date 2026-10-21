## Description:

Helps agents clone a voice from a clean audio sample for use with ElevenLabs text-to-speech through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to submit an authorized voice sample and create a custom voice for text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can be used to impersonate someone without consent.

Mitigation: Clone only voices you own or have explicit permission to use.

Risk: Audio samples supplied through the CLI may be uploaded to dLazy.

Mitigation: Avoid sensitive or third-party recordings unless dLazy's handling is acceptable to you.

Risk: A saved API key persists locally, and the supplied command examples are inconsistent.

Mitigation: Use DLAZY_API_KEY for one-off access if desired, and verify the CLI's actual options before running commands.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON results]

**Output Format:** [Markdown guidance with shell commands; CLI returns JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and an audio URL or local audio sample; asynchronous tasks can return a task identifier.]

## Skill Version(s):

1.3.31 (source: server-resolved release; supplied skill frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
