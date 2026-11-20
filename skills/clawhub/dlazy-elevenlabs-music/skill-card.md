## Description:

Generates original 10–300 second music from natural-language prompts using ElevenLabs music_v1, for background music, advertisements, and short-video soundtracks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to generate original music tracks for background audio, advertisements, and short-form video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The supplied security assessment notes a partial scan and a gap between the described music-generation purpose and commands observed by the scanner.

Mitigation: Review the skill and pinned CLI package before use, and confirm the command behavior matches the advertised task.

Risk: The skill says prompts and any local media supplied are sent to dLazy-hosted services.

Mitigation: Avoid sending confidential prompts or media unless the service's data handling meets your needs; use an API key you can rotate or revoke.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON, Shell commands]

**Output Format:** [JSON response with generated asset URLs; audio file when saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates 10–300 second tracks; asynchronous mode may return a task ID before the result is ready.]

## Skill Version(s):

1.3.43 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
