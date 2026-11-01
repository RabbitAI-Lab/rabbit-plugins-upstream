## Description:

Skill Factory helps agents design, build, package, and review new OpenClaw skills from a domain or task description.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and agent operators use this meta-skill to turn a target domain into a structured OpenClaw skill package with a SKILL.md, references, templates, README guidance, and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skills can contain broad triggers, excessive permission expectations, unclear data handling, or unsafe side effects if accepted without review.

Mitigation: Review each generated SKILL.md for narrow triggers, anti-triggers, permission needs, data handling, external services, and side effects before enabling it.

Risk: A skill creation workflow can overwrite existing skill files or include sensitive paths if the request is careless.

Mitigation: Confirm before overwriting existing skills, avoid token and credential files, and run a secret scan before treating generated skill output as ready.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-factory)
- [Skill Anatomy](references/skill-anatomy.md)
- [Skill Design Patterns](references/design-patterns.md)
- [Quality Framework](references/quality-framework.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [Skill Creation Template](templates/skill-creation-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with file structures, checklists, templates, and inline code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces skill package guidance and draft skill files for review before installation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
