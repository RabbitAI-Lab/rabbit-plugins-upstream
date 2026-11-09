## Description:

Generates short sound effects from text descriptions using the ElevenLabs text-to-sound model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative practitioners use this skill to generate short sound effects from text prompts for foley, ambience, alerts, and games.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a mismatch between the sound-effects purpose and the CLI login and authentication commands; the scan was partial and did not inspect the pinned CLI package.

Mitigation: Review the pinned @dlazy/cli package and confirm its authentication behavior before installing it or providing credentials.

## Reference(s):

- [CLI source link declared in skill metadata](https://github.com/dlazy-ai/cli)
- [CLI package declared in skill metadata](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON]

**Output Format:** [JSON result with generated sound-effect output URLs, optionally saved as an audio file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sound effects are 1–22 seconds; duration defaults to 5 seconds.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
