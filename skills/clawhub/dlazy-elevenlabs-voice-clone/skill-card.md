## Description:

Uploads a clean voice sample to clone a custom voice for use with ElevenLabs text-to-speech through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to authenticate with dLazy, submit a permitted voice sample, and create a custom ElevenLabs voice clone for TTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples and parameters are sent to third-party cloud processing.

Mitigation: Install only if this data transfer is acceptable; provide only intended audio paths and try the npx or dry-run flow first.

Risk: The skill stores a dLazy API key locally or reads it from DLAZY_API_KEY.

Mitigation: Protect the key, rotate or revoke it when it is no longer needed, and avoid exposing it in shared shells or logs.

Risk: Voice cloning can be misused without the speaker's permission.

Mitigation: Use only voice samples you are authorized to clone and confirm the intended use complies with applicable terms and policies.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; uploads selected audio to dLazy-hosted cloud endpoints.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
