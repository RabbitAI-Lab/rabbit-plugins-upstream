## Description:

Recruit CRM (recruitcrm.io). Use this skill for ANY Recruit CRM request - searching and reading data. Whenever a task involves Recruit CRM, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Recruiting, staffing, and operations users use this skill to search and read Recruit CRM candidates, companies, contacts, and jobs through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can direct users to install or authenticate the oo CLI before using the connector.

Mitigation: Use a verified or package-manager installation of the oo CLI, and avoid running pipe-to-shell setup commands blindly.

Risk: Recruit CRM requests and responses are processed through OOMOL-connected account infrastructure.

Mitigation: Install only if you trust OOMOL for this account and keep the Recruit CRM connection limited to read-only scopes when lookup and list tasks are the intended use.

Risk: Broad routing instructions tell the agent to use this skill for any Recruit CRM request.

Mitigation: Confirm user intent and inspect the live connector schema before running actions, especially if future actions include write or destructive tags.

## Reference(s):

- [Recruit CRM homepage](https://recruitcrm.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recruitcrm)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schema inspection before forming Recruit CRM action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
