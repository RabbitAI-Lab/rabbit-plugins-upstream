## Description:

Pipedrive (pipedrive.com). Use this skill for Pipedrive requests that read, create, update, or delete CRM records through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Pipedrive CRM records from an agent session using an OOMOL-connected account. It supports reading, listing, searching, creating, updating, and deleting deals, persons, organizations, activities, pipelines, and stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run a remote installer script for the oo CLI.

Mitigation: Install or approve the oo CLI from verified OOMOL documentation or a trusted package source before enabling the skill.

Risk: Write and destructive Pipedrive actions can change or delete CRM records.

Mitigation: Require explicit user confirmation of the target record, payload, and expected effect before create, update, or delete actions.

## Reference(s):

- [ClawHub Pipedrive skill page](https://clawhub.ai/oomol/skills/oo-pipedrive)
- [Pipedrive homepage](https://www.pipedrive.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill uses oo CLI connector schema and run commands; write and destructive operations require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
