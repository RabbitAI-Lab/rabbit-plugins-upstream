## Description:

Karakeep (karakeep.app). Use this skill for ANY Karakeep request: reading, creating, updating, and deleting data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate a connected Karakeep account from an agent, including bookmark, tag, list, feed, highlight, asset, backup, and administrative workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents running a remote installer script directly from the network.

Mitigation: Review the installer before use, prefer a versioned, signed, or checksum-verified oo CLI installation source, and avoid running the installer from an elevated shell.

Risk: The skill can perform state-changing and destructive Karakeep actions, including deleting bookmarks, feeds, lists, tags, highlights, backups, and asset records.

Mitigation: Confirm the exact action, payload, and target with the user before write or destructive operations, and inspect the live connector schema before constructing payloads.

## Reference(s):

- [Karakeep homepage](https://karakeep.app)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Karakeep skill](https://clawhub.ai/oomol/skills/oo-karakeep)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector command results, temporary file URLs, and confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
