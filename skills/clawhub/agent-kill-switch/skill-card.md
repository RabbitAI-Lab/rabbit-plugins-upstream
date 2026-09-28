## Description:

Creates a pre-deployment shutdown card documenting stop conditions, access-revocation actions, an owner, and recovery criteria, and checks that required fields are present.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only; documentation and theory all rights reserved)

## Use Case:

Developers and operations teams use this skill before deploying an agent to record shutdown triggers, revocation steps, a responsible person, and conditions for resuming operation. The local check verifies fields, not whether an agent can actually be stopped.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complete card could be mistaken for a working emergency stop.

Mitigation: Implement and test the actual shutdown and access-revocation controls separately before deployment.

Risk: Instructions and licensing terms may be misunderstood or reused outside their permitted scope.

Mitigation: Review the Chinese-language instructions and confirm rights for the documentation and theory before installing or redistributing.

## Reference(s):

- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/agent-kill-switch)

## Skill Output:

**Output Type(s):** [Text, JSON files, Guidance]

**Output Format:** [Plain-text status or JSON shutdown card and check result]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cards capture stop conditions, revocation actions, owner, recovery criteria, and creation date; checks report missing fields with a nonzero exit status.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
