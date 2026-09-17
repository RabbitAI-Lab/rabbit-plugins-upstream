## Description:

Automates Slite note and group operations through an OOMOL-connected Slite account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to read, search, create, update, and delete Slite notes and groups from an OOMOL-connected Slite account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes running a remote installer directly in a shell.

Mitigation: Review the oo CLI installation method before installing and prefer a verified or package-manager installation path if available.

Risk: Slite request payloads and responses are processed through OOMOL.

Mitigation: Connect Slite with the minimum permissions needed and confirm that routing Slite content through OOMOL is acceptable for the workspace.

Risk: Write and destructive actions can create, update, or delete Slite content.

Mitigation: Confirm the exact payload, target, and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-slite)
- [Slite homepage](https://slite.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON data, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Slite connector schemas before actions; write and delete actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
