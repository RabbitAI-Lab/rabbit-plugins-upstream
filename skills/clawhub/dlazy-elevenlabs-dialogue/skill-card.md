## Description:

Generates ElevenLabs eleven_v3 dialogue audio from multi-speaker lines with per-line voices and expressive audio tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to turn dialogue lines with assigned voices into multi-speaker audio for character scenes, podcasts, and short skits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dialogue and any selected media are processed by dLazy, and generation uses service credits.

Mitigation: Submit only content you are authorized to share with the service, and confirm expected credit use before generating.

Risk: Login saves an organization API key in the local CLI configuration.

Mitigation: Protect the local configuration and rotate or revoke the key if it may have been exposed.

Risk: Some skill examples may not match the dialogue command options.

Mitigation: Check `dlazy elevenlabs-dialogue -h` and review the parameters before generating.

## Reference(s):

- [dLazy service information](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project information (skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [Generated dialogue audio, with a JSON result containing output links or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dialogue supports up to 20 lines and 10 distinct voices; audio is returned through dLazy-hosted links.]

## Skill Version(s):

1.3.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
