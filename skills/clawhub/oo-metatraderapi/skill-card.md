## Description:

MetaTraderAPI lets agents operate MetaTraderAPI through OOMOL-connected accounts for account reads, market and history lookups, and session management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to route MetaTraderAPI tasks through the oo CLI, inspect live action schemas, read trading-account data, and manage MetaTraderAPI sessions with confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can install the oo CLI through an unverified remote installer.

Mitigation: Review the installation path first and prefer a verified or package-managed oo CLI installation before running installer commands.

Risk: The skill can access sensitive trading-account data and affect active MetaTraderAPI sessions.

Mitigation: Require explicit user confirmation before starting, stopping, or closing sessions, and confirm targets for destructive actions.

## Reference(s):

- [MetaTraderAPI homepage](https://metatraderapi.cloud/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-metatraderapi)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
