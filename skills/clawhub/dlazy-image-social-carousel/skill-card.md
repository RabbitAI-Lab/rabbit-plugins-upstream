## Description:

A structured workflow skill for planning social media carousels with a direction-confirmation and cover-first generation process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and social media teams use the skill to plan carousel structure, confirm a visual direction, and generate a cover before the remaining slides. It produces a structured slide plan and can use the dLazy CLI for image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media may be sent to dLazy services through the CLI; the security review also noted undeclared CLI authentication behavior and that some referenced material was unavailable.

Mitigation: Before use, confirm you intend to use dLazy authentication and cloud processing, avoid sending sensitive material, and review the CLI behavior and service terms.

## Reference(s):

- [CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)
- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-carousel)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured guidance, Image assets]

**Output Format:** [Markdown slide plan and confirmation table, followed by generated carousel images when the dLazy CLI flow is used]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a confirmation step before generation and a cover-first sequence for visual consistency.]

## Skill Version(s):

1.3.40 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
