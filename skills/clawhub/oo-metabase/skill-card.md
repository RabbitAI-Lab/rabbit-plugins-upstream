## Description:

Metabase connector skill for reading, creating, updating, and deleting Metabase data through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to inspect schemas, query Metabase content, and manage collections, dashboards, questions, and metrics through an OOMOL-connected Metabase account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Metabase content through an OOMOL-connected account.

Mitigation: Run read-only actions directly, but require user confirmation for actions tagged [write] and explicit approval for actions tagged [destructive].

Risk: Fallback setup includes remote shell and PowerShell installer commands for the oo CLI.

Mitigation: Do not run downloaded installer scripts unless the user has independently decided to trust the installer source.

## Reference(s):

- [ClawHub Metabase skill page](https://clawhub.ai/oomol/skills/oo-metabase)
- [Metabase homepage](https://www.metabase.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects that include data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
