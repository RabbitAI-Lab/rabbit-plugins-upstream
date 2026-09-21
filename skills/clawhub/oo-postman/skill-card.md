## Description:

Postman (postman.com). Use this skill for ANY Postman request: reading, creating, updating, and deleting data through an OOMOL-connected Postman account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API teams use this skill to manage Postman workspaces, collections, requests, APIs, schemas, environments, monitors, comments, and related collaboration workflows from an agent using the oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute an unpinned remote installer for the oo CLI.

Mitigation: Prefer a verified or manual oo CLI installation path and do not let the agent run the remote installer automatically.

Risk: The connector can access sensitive Postman account data and perform write or destructive operations.

Mitigation: Require explicit user confirmation for sensitive reads, writes, deletes, and payloads before running connector actions.

Risk: Broad Postman access depends on trusting OOMOL's connector and server-side credential handling.

Mitigation: Install only when the publisher and connector are trusted, and grant the minimum Postman access needed for the task.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-postman)
- [Postman](https://www.postman.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
