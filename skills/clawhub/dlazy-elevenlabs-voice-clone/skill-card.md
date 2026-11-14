## Description:

Requests an ElevenLabs Instant Voice Clone from a clean voice sample for use with ElevenLabs text-to-speech.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit a clean voice sample to request a custom voice for ElevenLabs text-to-speech. The skill invokes the dLazy CLI and returns a task result or generated output metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The partial scan did not demonstrate the claimed voice-cloning behavior and could not inspect some referenced paths or package details.

Mitigation: Review the actual CLI command behavior and the unavailable package or path details before relying on the skill.

Risk: The skill documentation says local audio files are uploaded to dLazy media storage and request parameters are sent to its hosted API.

Mitigation: Submit only voice recordings you are authorized to use, and review dLazy's service terms before sending audio.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-elevenlabs-voice-clone)
- [dLazy website](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI project link listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON task or result metadata, with status and output URLs when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task identifier for asynchronous work; the documented example shows an output URL.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
