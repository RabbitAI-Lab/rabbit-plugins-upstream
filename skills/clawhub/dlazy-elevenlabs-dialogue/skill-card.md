## Description:

Generates ElevenLabs eleven_v3 dialogue audio with up to 10 distinct voices across as many as 20 lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to turn scripted dialogue, podcasts, and short skits into multi-voice ElevenLabs audio, with optional emotion tags for each line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue text and any selected media are sent to dLazy for cloud processing.

Mitigation: Submit only content and media you are authorized to share, and review the inputs before generating audio.

Risk: Generation uses service credits, and login stores an API key in local CLI configuration.

Mitigation: Use dry-run to review the payload and estimated cost; protect the local configuration and rotate or revoke the key if it is exposed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-dialogue)
- [CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON result or task metadata]

**Output Format:** [Generated dialogue audio asset, returned as a URL or saved file, with JSON result metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports up to 20 dialogue lines and up to 10 unique voices; asynchronous task metadata is available when requested.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
