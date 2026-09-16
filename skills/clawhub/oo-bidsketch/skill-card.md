## Description:

BidSketch lets agents retrieve BidSketch clients, proposals, and proposal content through an authenticated OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to search and read data from an authenticated BidSketch account, including clients, proposals, proposal content, and proposals for a specific client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path tells users to run remote installer scripts directly in a shell.

Mitigation: Prefer the vendor installation documentation or an installation package with checksum or signature verification before running setup commands.

Risk: The skill relies on OOMOL as an intermediary for BidSketch account access.

Mitigation: Install and connect BidSketch only if OOMOL is an acceptable intermediary for the account and data being accessed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bidsketch)
- [BidSketch Homepage](https://www.bidsketch.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only BidSketch get and list actions; connector responses include action data and an execution identifier.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
