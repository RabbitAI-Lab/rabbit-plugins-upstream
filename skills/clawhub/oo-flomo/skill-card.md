## Description:

flomo (flomoapp.com). Use this skill for ANY flomo request -- reading, creating, updating, and deleting data. Whenever a task involves flomo, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate flomo through an OOMOL-connected account, including creating memos, searching and reviewing memos, managing tags, and retrieving memory context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute code on the user's machine.

Mitigation: Review the setup path before installing and use the installer only after independently verifying the official source and trusting OOMOL and flomo access through OOMOL.

Risk: Write or destructive connector actions can create, update, rename, or overwrite flomo data.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running actions marked write or destructive.

## Reference(s):

- [flomo homepage](https://flomoapp.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-flomo)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata; write and destructive actions require user confirmation before execution.]

## Skill Version(s):

1.0.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
