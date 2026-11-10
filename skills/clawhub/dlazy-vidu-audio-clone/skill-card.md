## Description:

Clone voice and generate new text reading audio with one click using Vidu Audio Clone. 使用 Vidu 声音克隆技术，通过参考音频一键复制音色并生成新文本的朗读音频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Users can provide reference audio and text through the dLazy CLI to generate spoken audio in a cloned voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local audio paths are uploaded to dLazy media storage, and prompts are sent to its hosted API.

Mitigation: Only submit recordings and text you are authorized to share; review dLazy's service terms before sending sensitive material.

Risk: The security review was partial and did not establish how the `dlazy login` command supports voice cloning.

Mitigation: Confirm the CLI flow before use; the benign verdict has medium confidence and is not a guarantee of safety.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy service](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI repository (linked in skill metadata; provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Audio, JSON]

**Output Format:** [CLI JSON response containing generated audio output links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio is generated from reference audio and text; asynchronous jobs may return a task identifier before the output is ready.]

## Skill Version(s):

1.3.38 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
