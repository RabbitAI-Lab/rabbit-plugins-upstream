## Description:

Generates 10–300 seconds of original music from natural-language prompts using the ElevenLabs music_v1 model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and media producers can use the skill to generate original background music, advertising music, or short-video soundtracks from natural-language prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review found that the login and authentication setup does not clearly match the advertised music-generation purpose; the scan was partial and did not inspect the external CLI package.

Mitigation: Before authenticating, review the CLI package and confirm you are comfortable with its behavior and the third-party service receiving your prompts.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-music)
- [CLI source link cited by the skill (not server-resolved provenance)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [Generated audio asset (download URL or saved file) with JSON task/result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Music duration is 10–300 seconds; asynchronous requests may return a task ID.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
