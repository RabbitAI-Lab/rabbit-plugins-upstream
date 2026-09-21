## Description:

Helps agents inspect Pinata action schemas and manage Pinata files, groups, pin requests, and CIDs through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate Pinata through an OOMOL-connected account, including reading, creating, updating, pinning, grouping, and deleting Pinata data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the oo CLI through a remote script can expose users to install-path or supply-chain risk.

Mitigation: Review OOMOL's official install guidance first and prefer a verified or package-manager installation path when available.

Risk: Write and destructive Pinata actions can change metadata, visibility, grouping, or delete Pinata files.

Mitigation: Fetch the live action schema, review the exact JSON payload and target identifiers, and obtain explicit user confirmation before state-changing actions.

Risk: Pinata actions depend on the user's OOMOL account connection, scopes, credentials, and billing state.

Mitigation: Use first-time setup steps only after matching command failures and direct the user to reconnect or resolve billing before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pinata)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Pinata homepage](https://pinata.cloud)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, JSON, Markdown guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands inspect live Pinata action schemas before execution and may return JSON responses containing data and an execution ID.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
