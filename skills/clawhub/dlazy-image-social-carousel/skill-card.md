## Description:

A structured workflow skill dedicated to social-media carousel design, using a single-confirmation and cover-first flow for planning and generating multi-slide social media image sets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and social media teams use this skill to plan social carousel structure, confirm the cover direction first, and generate remaining slides consistently through the dLazy CLI cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, generation parameters, and local media paths may be sent or uploaded to the dLazy cloud service.

Mitigation: Use this skill only when third-party cloud generation is acceptable, and avoid sending sensitive prompts or media unless approved for that service.

Risk: The dLazy API key can be stored persistently in the local CLI configuration.

Mitigation: Use the DLAZY_API_KEY environment variable for per-run authentication when a persistent key in ~/.dlazy/config.json is not desired.

Risk: Generated carousel images may still need review for factual accuracy, brand fit, and platform suitability before publication.

Mitigation: Review generated image URLs and requested slide copy before publishing or using them in external campaigns.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)
- [dLazy CLI Repository](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow guidance with confirmation tables and inline shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides dLazy CLI calls; generated images are returned as hosted URLs by the third-party service.]

## Skill Version(s):

1.3.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
