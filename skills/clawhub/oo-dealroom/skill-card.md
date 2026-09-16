## Description:

Dealroom lets agents search and read Dealroom company, investor, and transaction data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Dealroom companies, investors, and transactions from an OOMOL-connected account while relying on the live connector schema for payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path can run a live internet installer directly in a shell.

Mitigation: Install only after reviewing official install documentation, prefer pinned or verified installer artifacts where available, and require explicit approval before any CLI installation or login/connect step.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dealroom)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Dealroom homepage](https://dealroom.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live Dealroom connector schema before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
