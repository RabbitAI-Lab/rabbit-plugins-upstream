## Description:

Qlty (qlty.sh) helps an agent search and read Qlty data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Qlty connector schemas and run read-oriented Qlty actions through an OOMOL-connected account for users, workspaces, projects, project metrics, rate limits, and issue lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified internet installer commands for the oo CLI.

Mitigation: Install the CLI only from a trusted OOMOL distribution path, prefer a signed or pinned installer with checksum verification, and do not let an agent run curl-to-shell or PowerShell install commands automatically.

## Reference(s):

- [Qlty homepage](https://qlty.sh)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI qlty connector and expects JSON payloads that match live action schemas.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
