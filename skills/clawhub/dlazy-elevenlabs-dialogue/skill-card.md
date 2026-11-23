## Description:

Generate ElevenLabs eleven_v3 dialogue audio by assigning voices to individual lines, with support for expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and developers can create narrated character dialogue, podcast segments, and short skits with distinct voices for each line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment has medium confidence and incomplete evidence, with a reported mismatch between the stated dialogue-generation purpose and the commands observed by the scanner.

Mitigation: Before installing, review the CLI package and the section noted in the security guidance, and confirm the commands match your expectations.

Risk: The skill requires a dLazy API key and sends prompts to the hosted service; local media paths passed through supported media fields are uploaded to dLazy storage.

Mitigation: Only submit content you are authorized to share, and use dLazy account controls to rotate or revoke credentials when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON result metadata]

**Output Format:** [Generated dialogue audio asset with JSON result metadata and optional local file save]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 20 dialogue lines and 10 unique voices, expressive audio tags, language, stability, seed, and asynchronous generation.]

## Skill Version(s):

1.3.43 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
