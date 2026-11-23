## Description:

Image generation skill. Automatically selects the best dlazy CLI image model based on the prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users can describe an image task and have the agent choose a suitable dLazy image model for generation, editing, enhancement, or vectorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign but partial and notes video and speech features beyond the image-generation description.

Mitigation: Review the pinned CLI package and its available commands before use, and confirm that its media features fit your needs.

Risk: Prompts and supplied local media are sent to dLazy hosted services for processing and storage.

Mitigation: Avoid sending sensitive prompts or files unless you are comfortable with the service's handling of them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-generate)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Image assets, Image URLs, SVG]

**Output Format:** [Generated image outputs or hosted URLs; SVG for vector outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI returns JSON envelopes that can be piped into follow-on commands.]

## Skill Version(s):

1.3.44 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
