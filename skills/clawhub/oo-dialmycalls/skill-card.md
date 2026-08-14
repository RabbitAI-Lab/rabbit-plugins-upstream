## Description:

DialMyCalls (dialmycalls.com). Use this skill for ANY DialMyCalls request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage DialMyCalls account data through an OOMOL-connected account, including account lookup and contact or group create, read, update, list, and delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write actions can create or update DialMyCalls contacts and groups.

Mitigation: Confirm the exact action, payload, and expected account change with the user before running write operations.

Risk: Destructive actions can delete DialMyCalls contacts or groups.

Mitigation: Confirm the target identifier and get explicit approval before running delete operations.

Risk: Payloads that do not match the live connector schema can fail or affect the wrong fields.

Mitigation: Inspect the connector schema for the selected action before constructing and running the payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dialmycalls)
- [DialMyCalls Homepage](https://www.dialmycalls.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
