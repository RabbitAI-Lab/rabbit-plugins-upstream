## Description:

Guides agents through marketing brochure requirements, layout design, user approval, and mock-up delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and business teams can use the skill to plan brochures, organize content across panels, and create layouts and mock-ups. It covers common formats such as tri-folds, bi-folds, Z-folds, and booklets, with approval required before mock-up production.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports an undeclared dLazy CLI authentication workflow and external package invocation, with only partial scanner coverage.

Mitigation: Before installing, review whether the CLI authentication and package invocation fit your needs, and consult the linked package information.

Risk: The skill sends prompts to dLazy's hosted API and uploads supplied media files to its media storage for generation.

Mitigation: Avoid providing sensitive prompts or media unless you are comfortable sending them to dLazy's hosted services.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [CLI homepage linked in skill metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image assets]

**Output Format:** [Markdown guidance and generated brochure images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Brochure layouts and mock-ups follow the selected fold type; mock-ups use the user-approved layout as a reference.]

## Skill Version(s):

1.3.44 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
