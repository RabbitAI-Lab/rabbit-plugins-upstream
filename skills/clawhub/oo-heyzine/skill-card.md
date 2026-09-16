## Description:

Uses the OOMOL oo CLI to let agents read, create, update, and delete Heyzine flipbooks and bookshelves through a connected Heyzine account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with OOMOL-connected Heyzine accounts use this skill to inspect live connector schemas and manage flipbooks and bookshelves, including reads, writes, and explicit-approval destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands in first-time setup could execute changing code on a user's machine.

Mitigation: Review installer steps before installing, prefer verified official documentation or pinned signed packages, and avoid running curl|bash or irm|iex from an elevated shell.

Risk: Write and destructive Heyzine actions can change or remove flipbooks, bookshelf assignments, or social sharing metadata.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Heyzine skill page](https://clawhub.ai/oomol/skills/oo-heyzine)
- [Heyzine homepage](https://heyzine.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON payloads, and JSON command output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before constructing action payloads; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
