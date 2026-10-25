## Description:

Generates Midjourney-style images from prompts, with configurable aspect ratios, bot types, and grid or U1–U4 outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to generate artistic, stylized images through dLazy's hosted service, choosing an aspect ratio, generation bot, and grid or individual output. It returns image results or an asynchronous task reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media provided for generation may be sent to dLazy's hosted service.

Mitigation: Only submit prompts and media that are appropriate for cloud processing; avoid sensitive content.

Risk: The workflow depends on a third-party CLI and a saved dLazy API key.

Mitigation: Review the pinned dependency before installation, protect the API key, and rotate or revoke it if exposed.

Risk: Image generation may incur service costs.

Mitigation: Check pricing or available credits before submitting generation requests.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image URLs or downloaded image files, with a JSON result containing output and task details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may be asynchronous; results can be downloaded to a local path.]

## Skill Version(s):

1.3.32 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
