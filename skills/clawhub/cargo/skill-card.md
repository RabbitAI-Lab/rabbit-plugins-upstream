## Description:

Routes Cargo CLI tasks to the right skill and explains cross-domain workflows, resource identifiers, asynchronous runs, and common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this router to choose the right Cargo skill, understand how Cargo CLI domains and resource identifiers connect, and follow documented workflows without confusing similar operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine refreshes can update installed software before changes are reviewed.

Mitigation: Pin versions and disable routine refreshes when updates should be reviewed separately.

Risk: Session activity is recorded by default, and support reports may include credentials or customer data.

Mitigation: Opt out of session recording where privacy is needed; require sanitized previews and approval before sharing support reports.

## Reference(s):

- [Prerequisites](references/prerequisites.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow](references/uuid-flow.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes Cargo tasks and summarizes documented workflows, identifiers, and operational cautions.]

## Skill Version(s):

1.29.2 (source: skill frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
