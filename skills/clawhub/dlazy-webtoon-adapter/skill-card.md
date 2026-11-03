## Description:

Adapts web novels into Chinese webtoon plot breakdowns, episode outlines, and scripts, and guides user-approved image generation through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators use the skill to adapt Chinese-language web novels into structured webtoon plots and episode scripts. It can also prepare and run user-approved image-generation requests through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy's hosted API and media storage for processing.

Mitigation: Send only prompts and media approved for cloud processing, and remove sensitive content before submitting.

Risk: The guide saves an API key in local CLI configuration and contains conflicting CLI version references.

Mitigation: Protect or rotate the API key, and confirm the intended CLI version before installation or use.

## Reference(s):

- [dLazy CLI project (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Image-generation prompts, Shell commands, Configuration guidance, Generated image links]

**Output Format:** [Chinese-language Markdown, with structured plot and episode scripts, inline shell examples, and image result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides image generation one request at a time after user confirmation.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
