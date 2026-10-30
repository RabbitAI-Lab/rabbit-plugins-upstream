## Description:

ByteDance's next-generation video model: up to 30 seconds per clip with native 4K, substantially better instruction following and long-form narrative. Supports multi-modal references (image + video + audio) and first/last frame control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams can use this skill to generate videos from text prompts and image, video, or audio references, including first and last frame control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference media and prompts are sent to dLazy's cloud service for video generation.

Mitigation: Submit only media and prompts you are comfortable uploading to dLazy.

Risk: The CLI saves an organization API key in a local configuration file, and generation jobs may incur costs.

Mitigation: Protect the saved key, revoke it when it is no longer needed, and check generation costs before submitting jobs.

Risk: The pinned external CLI's executable contents were not included in this artifact.

Mitigation: Review the pinned CLI before installing it.

## Reference(s):

- [dLazy CLI project page](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, JSON]

**Output Format:** [Generated video files with JSON results and output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Up to 30 seconds per clip and 2160p resolution; generation can return an asynchronous task identifier.]

## Skill Version(s):

1.2.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
