## Description:

Alibaba Bailian qwen3-tts voice cloning. Upload a clean voice sample to clone a custom voice usable in subsequent TTS calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to submit a clean, authorized voice sample to the dLazy hosted service and create a custom voice for later text-to-speech calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends request data to a hosted service and may upload a local voice sample; scanner coverage of CLI authentication behavior was partial.

Mitigation: Before providing an API key, review the CLI installation and authentication steps and confirm its behavior. Upload only voice recordings you have permission to use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [dLazy homepage](https://dlazy.com)
- [CLI project link listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured API response with result metadata, output URLs, or an asynchronous task ID.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May complete asynchronously; --no-wait returns a task ID for status polling.]

## Skill Version(s):

1.3.38 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
