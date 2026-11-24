## Description:

Generates ElevenLabs eleven_v3 speech from prompts using 12 multilingual voices and adjustable stability, similarity, and style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators can turn prompts into spoken audio for dubbing, audiobooks, and character dialogue, choosing from multilingual voices and tuning speech characteristics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reported an undeclared dLazy CLI login/authentication step that may not clearly match the described ElevenLabs text-to-speech purpose.

Mitigation: Before installing or authenticating, review the dLazy login flow and confirm that the CLI and authentication flow are expected for this feature; the scan could not inspect the CLI package or resolve several local references.

## Reference(s):

- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio files, JSON result metadata]

**Output Format:** [Generated audio asset or task status returned by the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With --no-wait, the result may contain a task ID before audio is ready.]

## Skill Version(s):

1.3.44 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
