## Description:

Helps an agent read and manage local Apple app data on macOS through a native Swift MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and developers use this skill to find and manage calendar events, reminders, contacts, messages, mail, notes, photos, and local Music playlists through an agent. It requires macOS 14 or later and is distributed for Apple Silicon Macs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to private Apple app data can expose sensitive personal information.

Mitigation: Review macOS permission prompts carefully and allow read-only tools where possible.

Risk: Sends, deletions, and playlist rewrites can make consequential or irreversible changes.

Mitigation: Require user confirmation and review the proposed action before granting write access.

Risk: Installing the MCP package grants an agent powerful local app access.

Mitigation: Verify the GitHub release before installing the package.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [MCP package releases](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups and permission-gated actions; selected sends, deletes, and playlist changes require confirmation.]

## Skill Version(s):

2.4.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
