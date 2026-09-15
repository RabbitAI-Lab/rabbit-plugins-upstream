## Description:

Enables an agent to operate Dropbox through OOMOL's oo CLI using a connected Dropbox account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, search, list, download, upload, move, copy, restore, delete, and share Dropbox files through a connected OOMOL account. It is suited to Dropbox file-management workflows where write and destructive actions are confirmed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute unreviewed code on a user's machine.

Mitigation: Prefer a reviewed, pinned, or package-managed oo CLI installation method instead of running curl-to-bash or PowerShell installer commands blindly.

Risk: Write and destructive Dropbox actions can change, remove, or overwrite user data.

Mitigation: Confirm exact payloads, paths, and effects with the user before write actions, and require explicit approval before delete, revoke, or overwrite operations.

## Reference(s):

- [ClawHub Dropbox skill page](https://clawhub.ai/oomol/skills/oo-dropbox)
- [Dropbox homepage](https://www.dropbox.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When actions are executed, the oo connector returns JSON data with execution metadata.]

## Skill Version(s):

1.0.5 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
