## Description:

Submit a clean voice sample to request an ElevenLabs Instant Voice Clone for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use the dLazy CLI to submit a clean audio sample and request a custom voice for ElevenLabs text-to-speech.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release scan could not verify that this skill performs the advertised voice-cloning workflow, and it could not determine what happens during dLazy login.

Mitigation: Before supplying credentials or voice samples, review the CLI source and confirm how login and audio uploads are handled; use the command's --dry-run option to inspect a request when supported.

## Reference(s):

- [CLI repository linked by the skill documentation](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Audio]

**Output Format:** [JSON API response with task status and generated output metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task identifier for asynchronous jobs; the release scan did not demonstrate the advertised voice-cloning result.]

## Skill Version(s):

1.3.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
