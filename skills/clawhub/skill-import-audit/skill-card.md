## Description:

Use before trusting a downloaded skill: audit it first.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blueboyzx](https://clawhub.ai/user/blueboyzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use this agent skill to vet downloaded or third-party skills before trusting or installing them, reviewing integrity, security, portability, and correctness in that order.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was only partially complete because two local path-like references in SKILL.md could not be resolved.

Mitigation: Resolve and review those references, then scan their contents before relying on the audit or installing the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/blueboyzx/skills/skill-import-audit)
- [ClawHub Search & Candidate Comparison](references/clawhub-search-and-compare.md)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Shell commands]

**Output Format:** [Markdown audit findings with supporting evidence and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four ordered review phases: provenance, security, portability, and correctness.]

## Skill Version(s):

1.0.1 (source: frontmatter; ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
