## Description:

Signalbase helps agents search and read Signalbase company profiles, investor records, and market signals through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to browse and search Signalbase companies, investors, acquisition signals, funding signals, hiring signals, and job-change signals from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Review installation commands before use and prefer verified official release documentation, a trusted package manager, or installers with checkable signatures or checksums; do not allow an agent to run remote installers automatically.

Risk: Connector calls can fail when authentication, scopes, app connection, credentials, or billing state are missing or expired.

Mitigation: Run setup or recovery commands only after a matching failure and confirm connection or billing remediation with the user before retrying.

## Reference(s):

- [Signalbase homepage](https://www.trysignalbase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON, Configuration guidance]

**Output Format:** [Markdown summaries with oo CLI commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
