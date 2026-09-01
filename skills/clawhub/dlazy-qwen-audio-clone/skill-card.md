## Description:

Creates a reusable Alibaba Bailian Qwen3-TTS custom voice by uploading a clean voice sample through dLazy's hosted voice-cloning service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to create a named cloned voice from an authorized audio sample for later text-to-speech workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are sensitive and may be uploaded to dLazy cloud endpoints for cloning.

Mitigation: Use only audio samples with the speaker's informed consent and avoid uploading confidential or unauthorized voice data.

Risk: The dLazy API key may be persisted in ~/.dlazy/config.json after login or manual setup.

Mitigation: Prefer per-invocation credentials when practical, review local config file permissions, and rotate or revoke the key if exposure is possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON]

**Output Format:** [JSON result from the dLazy CLI, with command examples and authentication guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; local audio paths may be uploaded to dLazy cloud storage; asynchronous runs can return a task identifier for polling.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter: 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
