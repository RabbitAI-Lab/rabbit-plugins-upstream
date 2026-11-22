## Description:

Creates a reusable custom Qwen3-TTS voice from a clean voice sample through Alibaba Bailian.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to submit a clean voice sample and create a custom voice for later Qwen3-TTS calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete: it reports an unexplained `dlazy login` command and could not resolve several referenced paths or establish what login accesses.

Mitigation: Before installing, review the CLI install and account requirements and confirm what `dlazy login` accesses before authorizing it.

Risk: Local audio supplied to the skill is uploaded to dLazy media storage for processing.

Mitigation: Use only voice samples you are authorized to share, and avoid uploading private recordings unless cloud processing is acceptable.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy service](https://dlazy.com)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Voice profile]

**Output Format:** [JSON response with the custom voice result or asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A created custom voice is intended for later text-to-speech calls.]

## Skill Version(s):

1.3.41 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
