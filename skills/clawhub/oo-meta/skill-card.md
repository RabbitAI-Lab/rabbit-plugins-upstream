## Description:

Meta (business.meta.com). Use this skill for ANY Meta request - searching and reading data. Whenever a task involves Meta, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Meta through an OOMOL-connected account, including retrieving the current user, listing ad accounts and campaigns, and getting Meta Ads insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes one-line remote installer commands.

Mitigation: Use an official, versioned installer with checksum or signature verification before installing the oo CLI.

Risk: The skill routes broad Meta requests through a connected account that can expose business data.

Mitigation: Use it only for Meta account-data tasks and install it only when OOMOL is trusted with the connected Meta business data.

Risk: Future connector actions may change Meta state if write or destructive actions are added.

Mitigation: Inspect the live action schema and confirm write or destructive payloads with the user before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-meta)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Meta Business](https://business.meta.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
