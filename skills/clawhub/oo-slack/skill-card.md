## Description:

Connects agents to Slack through an OOMOL account to read workspace information and manage messages, reactions, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with an OOMOL-connected Slack account use this skill to find workspace information, exchange messages, and manage files and reactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running a remotely downloaded installer directly in a shell without verification.

Mitigation: Prefer a verified package manager or signed release, or inspect the installer before running it.

Risk: The connected account can expose Slack workspace data to OOMOL.

Mitigation: Review OOMOL's access to the workspace before connecting the account.

Risk: Write and delete actions can change or remove Slack content.

Mitigation: Confirm each action's exact target and effect; obtain explicit approval before deletion.

## Reference(s):

- [ClawHub Slack skill listing](https://clawhub.ai/oomol/skills/oo-slack)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Text or Markdown with Slack action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the connected account's Slack access.]

## Skill Version(s):

1.0.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
