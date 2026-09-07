## Description:

Part of the Overpowered skill suite, this skill helps agents simulate workflows, migrations, bulk updates, automations, or other side-effecting operations before committing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[raguets](https://clawhub.ai/user/raguets)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation maintainers use this skill to preview broad, costly, irreversible, externally visible, or hard-to-audit changes before live execution. It produces a dry-run scope, predicted changes, exceptions, human gates, invariant checks, and a go/no-go recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A dry run may accidentally perform real side effects such as sending notifications or writing production data.

Mitigation: Block or redirect externally visible side effects and explicitly state which side effects cannot be simulated faithfully.

Risk: A simulation can miss material edge cases or produce misleading approval evidence.

Mitigation: Use representative inputs, include exceptions and invariant checks, and stop for revision when the predicted effects are surprising.

## Reference(s):

- [Overpowered suite](https://github.com/raguets/overpowered)
- [ClawHub skill page](https://clawhub.ai/raguets/skills/dry-run)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text dry-run report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected sections include dry-run scope, predicted changes, exceptions, human gates, invariant checks, and go/no-go recommendation.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
