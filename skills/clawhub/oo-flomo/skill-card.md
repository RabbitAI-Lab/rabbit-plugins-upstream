## Description:

Use flomo through an OOMOL-connected account to read, create, update, search, and manage memos and tags via the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their connected flomo workspace from an agent, including memo search, memo creation and updates, tag management, daily review retrieval, and related memo recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to run remote installer scripts in a shell.

Mitigation: Review setup steps before installing, prefer a verifiable official package or an inspected installer script, and do not let an agent run the remote installer automatically.

Risk: Write actions can create or change flomo memos and tags.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions such as create_memo, memo_update, or tag_rename.

## Reference(s):

- [flomo homepage](https://flomoapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-flomo)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
