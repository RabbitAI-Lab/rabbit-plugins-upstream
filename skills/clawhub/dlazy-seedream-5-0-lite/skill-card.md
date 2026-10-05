## Description:

Generates images from text prompts or reference images using Doubao Seedream 5.0 Lite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to generate images from written prompts or supplied reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local images are sent to a third-party cloud service.

Mitigation: Only submit prompts and files you are authorized to share with dLazy.

Risk: The third-party CLI can be installed persistently and login saves an API key locally.

Mitigation: Review the pinned CLI before installation, use the on-demand npx option if preferred, and protect or rotate stored API keys.

## Reference(s):

- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, Image links]

**Output Format:** [JSON response with generated image URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be downloaded to a local path on request.]

## Skill Version(s):

1.3.24 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
