## Description:

Postman automation through an OOMOL-connected account for reading, creating, updating, and deleting Postman data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API teams use this skill to operate Postman workspaces, collections, requests, environments, APIs, schemas, mock servers, monitors, webhooks, forks, and pull requests through the OOMOL Postman connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes unverified remote installer one-liners that execute directly in a shell.

Mitigation: Use official, versioned installation instructions and verify checksums or signatures before installing the CLI.

Risk: The OOMOL Postman connector can perform broad read, write, and delete actions against a connected Postman account.

Mitigation: Grant access only when that scope is acceptable, confirm write and destructive actions before execution, and review sensitive read results before sharing them.

## Reference(s):

- [ClawHub Postman Skill](https://clawhub.ai/oomol/skills/oo-postman)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Postman](https://www.postman.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Postman connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
