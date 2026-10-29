## Description:

Generates videos with Tongyi Wanxiang 2.7 from text prompts, reference media, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use the skill to generate short videos from text prompts, reference media, or first and last frames through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy for processing, and local media is uploaded to its media storage.

Mitigation: Avoid submitting sensitive prompts or media, and upload only media you are authorized to share.

Risk: Login stores an API key in the local CLI configuration.

Mitigation: Use a trusted device, review the pinned CLI package before installation, and rotate or revoke the key when it is no longer needed.

Risk: Video generation can consume account credits.

Mitigation: Use the documented dry-run option to preview the request and estimated cost before generation.

## Reference(s):

- [CLI project page (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video files, JSON]

**Output Format:** [JSON response with generated media URLs; optionally a saved video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return an asynchronous task ID; generation settings include prompt, media inputs, resolution, duration, and prompt rewriting.]

## Skill Version(s):

1.3.34 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
