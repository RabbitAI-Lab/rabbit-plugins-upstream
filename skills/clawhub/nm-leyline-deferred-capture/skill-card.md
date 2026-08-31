## Description:

Defines the contract for deferred-item capture across plugins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent-skill maintainers use this skill to define and validate deferred-capture wrapper behavior, including CLI arguments, issue templates, labels, duplicate detection, and dry-run compliance output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wrappers built from this contract may create persistent GitHub issues.

Mitigation: Confirm the target repository, title, context, labels, branch, session ID, and artifact path before live use; use --dry-run for validation or testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-leyline-deferred-capture)
- [Leyline plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown guidance with CLI examples and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes required and optional CLI fields, issue body structure, label taxonomy, duplicate detection behavior, and dry-run compliance expectations.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
