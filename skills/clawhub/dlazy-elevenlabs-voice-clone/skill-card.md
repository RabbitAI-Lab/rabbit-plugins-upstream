## Description:

Helps agents use dLazy's ElevenLabs Instant Voice Cloning to create a custom voice from a clean voice sample for text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide voice-cloning requests using a permitted voice sample and a dLazy account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are sensitive and may be sent to dLazy or ElevenLabs-related services.

Mitigation: Use only your own voice or a voice you have explicit permission to clone, and confirm you are comfortable uploading the sample before use.

Risk: Saved API credentials on shared machines may be exposed to other users.

Mitigation: Prefer per-invocation credentials on shared machines.

Risk: Published command examples and the sample output schema are inconsistent with voice cloning.

Mitigation: Check the installed CLI's help and actual response before relying on examples or automating the output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON result guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI may return result metadata or an asynchronous task ID; verify its actual response.]

## Skill Version(s):

1.3.21 (source: ClawHub release evidence; skill frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
