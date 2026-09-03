## Description:

Simulate a workflow, migration, bulk update, automation, or other side-effecting operation before committing changes when effects are broad, costly, irreversible, externally visible, or difficult to audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill to preview side effects before running risky workflows, migrations, bulk updates, automations, or notification flows. It helps produce an explicit dry-run scope, predicted changes, exceptions, invariant checks, human gates, and a go/no-go recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dry-run report can be misleading if the simulation still writes data, sends real messages, or triggers production side effects.

Mitigation: Verify that dry-run mode blocks or redirects writes, notifications, and other externally visible side effects before relying on the report.

Risk: A dry run can miss material edge cases or side effects that cannot be simulated faithfully.

Mitigation: Use representative edge cases, check business invariants, and state any side effects that cannot be simulated.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text]

**Output Format:** [Markdown or structured text dry-run report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dry-run scope, predicted changes, exceptions, human gates, invariant checks, and go/no-go recommendation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
