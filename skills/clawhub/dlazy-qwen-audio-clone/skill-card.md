## Description:

Creates a reusable custom voice for Alibaba Bailian Qwen3-TTS from a clean voice sample.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create a custom voice from an authorized voice sample for subsequent text-to-speech calls. It invokes the dLazy service for Alibaba Bailian Qwen3-TTS voice cloning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice samples are uploaded through dLazy and may contain personal or third-party voice data.

Mitigation: Use only recordings you have permission to clone, and review dLazy's privacy terms before uploading.

Risk: Service use may consume credits, and some command examples may be inaccurate.

Mitigation: Check `dlazy qwen-audio-clone -h` before use, review any cost estimate, and consider `DLAZY_API_KEY` instead of saving the key in CLI configuration.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-qwen-audio-clone)
- [CLI repository listed in skill metadata (provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Audio, JSON, Guidance]

**Output Format:** [CLI JSON response with custom-voice creation status and result metadata; may include an asynchronous task status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a reusable custom voice; asynchronous runs may return a task identifier before completion.]

## Skill Version(s):

1.3.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
