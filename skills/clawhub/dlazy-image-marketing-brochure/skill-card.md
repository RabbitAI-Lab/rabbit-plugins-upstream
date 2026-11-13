## Description:

A complete workflow skill for marketing brochure design, covering everything from requirements gathering and layout design to mock-up delivery, using a layout-first process with a mandatory confirmation gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and designers use this skill to gather brochure requirements, plan content and panel layouts for different fold types, and develop brochure artwork. It guides layout iteration and approval before creating folded and lifestyle mock-ups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports medium confidence and partial coverage; use of an external CLI and authentication steps are not fully assessed by the available scan.

Mitigation: Review the CLI and its requested access before installation, and configure or rotate the dLazy API key through the account controls described by the skill.

## Reference(s):

- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)

## Skill Output:

**Output Type(s):** [Guidance, Image generation prompts, Images]

**Output Format:** [Markdown guidance and generated brochure artwork and mock-up images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image outputs use the requested brochure format; the documented default aspect ratio is 4:3. Mock-ups follow explicit user approval of the layout.]

## Skill Version(s):

1.3.41 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
