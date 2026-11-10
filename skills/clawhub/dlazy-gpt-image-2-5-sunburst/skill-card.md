## Description:

GPT Image 2.5 Sunburst generates and edits images, with support for reference images, detailed composition, in-image text, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to create or edit images from a text prompt and optional reference images, then receive the generated image or its hosted URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and any supplied local images are sent to dLazy services for generation or editing.

Mitigation: Avoid sending sensitive prompts or media unless sharing them with dLazy is appropriate for your use case.

Risk: The security review had partial coverage and could not assess the referenced CLI package; the skill uses a CLI login step.

Mitigation: Review the CLI package and its login behavior before installing or authenticating, and use an account and API key you are authorized to use.

## Reference(s):

- [dLazy](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)

## Skill Output:

**Output Type(s):** [Images, API response JSON]

**Output Format:** [Generated image files or hosted image URLs, with JSON result or task metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a prompt and up to five reference images, with aspect-ratio and quality options; asynchronous tasks can return a task ID.]

## Skill Version(s):

1.2.28 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
