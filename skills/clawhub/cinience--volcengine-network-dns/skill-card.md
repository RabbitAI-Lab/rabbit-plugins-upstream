## Description:

DNS record management on Volcengine networking services for zone record queries and updates, traffic routing changes, and DNS propagation troubleshooting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cinience](https://clawhub.ai/user/cinience)

### License/Terms of Use:


## Use Case:

Developers and infrastructure operators use this skill to query, update, and verify Volcengine DNS records while preserving change scope and rollback context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DNS changes can affect live services if applied to the wrong zone, record, or value.

Mitigation: Confirm the intended Volcengine DNS zones, review proposed DNS diffs and rollback values, and restrict agent access before changing production records.

## Reference(s):

- [Sources](references/sources.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with operational checklists and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes proposed DNS diffs, rollback values, TTL considerations, and propagation checks.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
