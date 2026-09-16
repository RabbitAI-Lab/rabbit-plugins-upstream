## Description:

Provides guidance and shell commands for reading Whop users, companies, memberships, and products through an OOMOL-connected Whop account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve Whop authorized users, companies, memberships, and products by ID or supported filters through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include running internet-hosted installers directly in a shell.

Mitigation: Review, pin, or verify the oo CLI installer before running it, and do not allow an agent to run curl-to-shell or PowerShell pipe installers unattended.

Risk: Whop data access depends on the connected OOMOL account and its available scopes.

Mitigation: Confirm the connected account, scope, and intended Whop data before retrieving users, companies, memberships, or products.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-whop)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Whop Homepage](https://whop.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect live connector schemas before forming JSON payloads and may summarize returned Whop data.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
