## Description:

Ringover (ringover.com). Use this skill for searching and reading Ringover data through the OOMOL oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Ringover connector schemas and retrieve Ringover calls, users, groups, IVRs, numbers, tags, and team details from an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance includes unverified remote installer scripts executed directly in a shell.

Mitigation: Review the skill before installation and use a signed or checksum-verified oo CLI installation path before running installer commands.

## Reference(s):

- [ClawHub Ringover Skill](https://clawhub.ai/oomol/skills/oo-ringover)
- [Ringover homepage](https://www.ringover.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution; read actions return JSON data with an execution id in meta.executionId.]

## Skill Version(s):

1.0.2 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
