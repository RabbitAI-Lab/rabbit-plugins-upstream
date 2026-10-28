## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from a shell using fpx to capture a signed-in browser token and curl for API requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OFW users use this skill to retrieve and manage family records from shell scripts without installing the ofw-mcp server. It requires a signed-in browser session and can send, change, upload, or delete records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending, changing, uploading, or deleting records can affect sensitive family-court information and may be permanent or visible to a co-parent.

Mitigation: Require explicit user approval before sending, deleting, changing expenses or visibility, uploading shared files, or creating journal entries; use an integration with enforced read-only limits for retrieval alone.

Risk: Opening an unread message can mark it read, and browser pairing remains active until revoked.

Mitigation: Avoid fetching unread message details unless marking them read is intended, and revoke browser pairing when access is no longer needed.

## Reference(s):

- [OurFamilyWizard requests reference](references/requests.md)
- [OurFamilyWizard web app](https://ofw.ourfamilywizard.com)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension information](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples and jq filters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples include commands that read and modify OurFamilyWizard records.]

## Skill Version(s):

2.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
