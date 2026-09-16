## Description:

Qlty (qlty.sh). Use this skill for ANY Qlty request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Qlty connector schemas and run read-oriented Qlty actions through an OOMOL-connected account, including retrieving users, workspaces, projects, metrics, rate-limit status, and issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands, and the security evidence flags this as suspicious when run without verification or clear user approval.

Mitigation: Avoid letting an agent run the remote installer automatically; review or use official, signed, versioned installation instructions before running setup commands.

## Reference(s):

- [Qlty homepage](https://qlty.sh)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qlty)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to fetch live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
