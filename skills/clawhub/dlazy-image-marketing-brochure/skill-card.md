## Description:

Guides marketing brochure design from requirements and layout planning through approved layouts, folded mock-ups, and lifestyle images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing and design teams use this skill to plan promotional brochures, create panel layouts, and develop folded and lifestyle mock-ups after layout approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to third-party dLazy services.

Mitigation: Avoid confidential unreleased materials unless the service is trusted and upload is approved.

Risk: The dLazy CLI may persist an API key locally, and the artifact contains a CLI version typo in its provenance text.

Mitigation: Consider an environment variable or on-demand npx use for less persistence, and review the package and its pinned version before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-marketing-brochure)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image URLs]

**Output Format:** [Markdown with layout plans, image links, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit approval of the layout before folded or lifestyle mock-ups.]

## Skill Version(s):

1.3.24 (source: ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
