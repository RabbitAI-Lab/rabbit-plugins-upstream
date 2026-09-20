## Description:

Bitbucket helps agents read, create, update, and delete Bitbucket resources through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Bitbucket repositories, pull requests, branches, commits, tags, workspaces, projects, snippets, and Pipelines through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An OOMOL-connected account can read and change Bitbucket resources through this skill.

Mitigation: Install only when that account access is acceptable, and use the least privileged connected account practical for the task.

Risk: Write and destructive actions can change repository state, delete repositories or branches, merge or decline pull requests, stop pipelines, or alter pipeline variables.

Mitigation: Confirm the exact target, payload, and effect with the user before running any write or destructive action.

Risk: Untrusted installation commands for the oo CLI could introduce supply-chain risk.

Mitigation: Use a trusted and verified oo CLI installation method instead of blindly running remote installer commands.

## Reference(s):

- [ClawHub Bitbucket Skill Page](https://clawhub.ai/oomol/skills/oo-bitbucket)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Bitbucket](https://bitbucket.org)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; write and destructive Bitbucket actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
