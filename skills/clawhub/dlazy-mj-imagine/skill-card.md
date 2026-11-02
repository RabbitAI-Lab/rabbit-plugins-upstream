## Description:

Generates Midjourney-style images from prompts with selectable aspect ratios, bot types, and grid or individual outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative users can generate stylized images from text prompts and select an aspect ratio, Midjourney or Niji Journey mode, and grid or individual U1–U4 output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy's hosted service for processing.

Mitigation: Avoid sending sensitive prompts or files unless you trust the service to process them.

Risk: Generation uses service credits, and authentication stores an API key locally.

Mitigation: Review the request and expected cost before generation, protect the local key, and revoke it from the dashboard when it is no longer needed.

## Reference(s):

- [CLI project page listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON]

**Output Format:** [Generated image URLs and output metadata in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation is controlled by the prompt, aspect ratio, bot type, and grid or U1–U4 output selection.]

## Skill Version(s):

1.3.35 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
