## Description:

Loomio (loomio.com). Use this skill for searching and reading Loomio poll data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Loomio connector schemas and run read-only Loomio poll workflows, including fetching a poll and listing polls in a group.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that can execute changing external code with the user's privileges.

Mitigation: Prefer a trusted, verified oo CLI installation method and avoid the curl-to-bash or PowerShell iex commands unless the installer endpoint is trusted.

Risk: Connector actions depend on live schemas and account connections, so stale assumptions can produce incorrect payloads or failed requests.

Mitigation: Fetch the action schema with oo connector schema before constructing payloads, and use first-time setup steps only after an auth or connection failure.

## Reference(s):

- [ClawHub Loomio Skill](https://clawhub.ai/oomol/skills/oo-loomio)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Loomio Homepage](https://www.loomio.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
