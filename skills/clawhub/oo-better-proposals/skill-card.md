## Description:

Use this skill for Better Proposals requests involving reading, creating, and updating account data through OOMOL's Better Proposals connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect and manage Better Proposals account resources, including proposals, quotes, companies, currencies, templates, settings, and brand details. The skill routes actions through OOMOL's Better Proposals connector and asks the agent to fetch the live action schema before building payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path may lead an agent to run remote installer commands directly in a shell.

Mitigation: Do not allow the agent to run remote installer commands automatically; install the oo CLI through a verified package or manually reviewed installer.

Risk: The skill operates through OOMOL as an intermediary for a Better Proposals account.

Mitigation: Use the skill only when that intermediary is acceptable, and limit agent actions to clearly requested Better Proposals tasks.

Risk: Better Proposals actions can read account and proposal data, and tagged write or destructive actions can change account state.

Mitigation: Confirm the exact payload and intended effect before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-better-proposals)
- [Better Proposals Homepage](https://betterproposals.io)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector action responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a live connector schema lookup before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
