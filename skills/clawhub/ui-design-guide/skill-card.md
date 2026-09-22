## Description:

Use when users need visual direction, interface hierarchy, layout decisions, design specifications, or prototypes before implementing a Web or mini program UI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to define visual direction, interface hierarchy, typography, color, layout strategy, and design specifications before building Web or mini program interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may direct agents to download remote UI assets through shell commands, which can expose users to untrusted URLs or unsuitable output paths.

Mitigation: Review asset URLs and destination paths before allowing downloads, avoid private or internal URLs, and prefer locally supplied or trusted assets when possible.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/binggg/skills/ui-design-guide)
- [UI Design Activation Checklist](checklist.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown with design specifications, implementation guidance, code examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose downloading remote UI assets; review URLs and output paths before execution.]

## Skill Version(s):

1.18.53 (source: server release metadata; artifact frontmatter declares 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
