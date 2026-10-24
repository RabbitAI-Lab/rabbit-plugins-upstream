## Description:

Generates videos with ByteDance's Seedance 2.5 model, supporting clips up to 30 seconds, native 4K, multimodal references, and first/last-frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and developers use this skill to generate videos from text prompts, optionally guided by reference images, videos, audio, or first and last frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected local image, video, or audio files are uploaded to dLazy for processing.

Mitigation: Only submit media you are authorized and comfortable sending to the service.

Risk: Video generation uses a paid API and may incur costs.

Mitigation: Review generation settings and estimated costs before submitting requests.

Risk: The API key is stored in the local CLI configuration unless supplied per invocation.

Mitigation: Protect the configuration file and rotate or revoke the key if it may be exposed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-5)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands]

**Output Format:** [Generated video assets referenced by URLs, with a JSON task/result envelope.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous runs can return a task ID; available duration and resolution depend on the request.]

## Skill Version(s):

1.2.29 (source: server-resolved release metadata; artifact frontmatter states 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
