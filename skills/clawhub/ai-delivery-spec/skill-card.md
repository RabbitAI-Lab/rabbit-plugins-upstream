## Description:

Helps teams clarify, specify, review, and change product, service, and office workflow requirements, PRDs, and interactive prototypes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

MIT

## Use Case:

Product and delivery teams, designers, engineers, and reviewers use this skill to turn vague ideas or existing requirements into scoped decisions, reviewable specifications, prototypes, change records, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project requirements and prototypes may contain sensitive data.

Mitigation: Avoid including raw secrets in project artifacts.

Risk: Optional checks may inspect unintended local files.

Mitigation: Run check and gate commands only on files you intend the skill to inspect.

Risk: Domain-rule, legal, or medical conclusions may be inaccurate or outdated.

Mitigation: Verify consequential conclusions against current authoritative sources.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [Requirement discovery guidance](artifact/references/discover.md)
- [Specification guidance](artifact/references/specify.md)
- [Change and acceptance guidance](artifact/references/change-acceptance.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Code, Shell commands]

**Output Format:** [Markdown specifications and review notes; optional YAML or JSON records, HTML prototypes, and validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested scope; validation results do not establish production readiness.]

## Skill Version(s):

5.5.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
