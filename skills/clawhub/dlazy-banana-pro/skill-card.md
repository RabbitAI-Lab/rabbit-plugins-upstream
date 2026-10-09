## Description:

Helps agents generate and edit images with Nano Banana Pro from text prompts or reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users use this skill to create or edit images from prompts and optional reference images through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and any supplied local images are sent to the third-party dLazy service.

Mitigation: Avoid submitting sensitive prompts or images unless sharing them with dLazy is acceptable.

Risk: Image generation may consume paid dLazy credits.

Mitigation: Check the cost estimate with the dry-run option and confirm available credits before generating.

Risk: Authentication can persist an API key locally, and global installation keeps the CLI on the system.

Mitigation: Use a per-invocation API key and the pinned npx option if persistent configuration or global installation is undesirable.

## Reference(s):

- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands; image-generation results are returned as JSON with image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image results can be saved locally; asynchronous requests can return a task ID.]

## Skill Version(s):

1.2.29 (source: ClawHub release metadata; supplied skill frontmatter says 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
