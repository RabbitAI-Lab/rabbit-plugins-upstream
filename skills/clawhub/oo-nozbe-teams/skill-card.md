## Description:

Nozbe connector skill for reading, creating, updating, and deleting Nozbe teams, projects, tasks, and comments through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Nozbe workspaces through an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting teams, projects, tasks, and comments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote script execution for installing the oo CLI.

Mitigation: Review the CLI installation path before installing and prefer official package instructions with verification.

Risk: Write and destructive actions can change or delete Nozbe projects, tasks, and comments.

Mitigation: Check the exact target and payload, then require explicit user confirmation before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nozbe-teams)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Nozbe homepage](https://nozbe.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads live connector schemas before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: evidence.json release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
