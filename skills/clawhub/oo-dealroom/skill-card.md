## Description:

Dealroom helps agents search and read Dealroom company, investor, and transaction data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Dealroom companies, investors, and transactions through an OOMOL-connected Dealroom account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote oo CLI installer scripts without pinning or checksum verification.

Mitigation: Review the installer before running it, or use a pinned, checksummed, or package-manager installation path when available.

Risk: Dealroom connector actions operate through the user's connected account, and write-capable actions should not run without clear intent.

Mitigation: Limit ordinary use to search/read actions, inspect the live action schema before building payloads, and require explicit user approval for any write or destructive action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-dealroom)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Dealroom Homepage](https://dealroom.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live connector schemas before constructing Dealroom action payloads.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
