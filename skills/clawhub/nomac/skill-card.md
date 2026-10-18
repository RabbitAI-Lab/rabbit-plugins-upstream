## Description:

Guides agents through using a cloud Mac for macOS and iOS development, including project sync, Xcode builds, and retrieving results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gergomiklos](https://clawhub.ai/user/gergomiklos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and their agents use this skill to access a cloud Mac, run macOS and Xcode workflows, transfer project files, and retrieve build results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The remote Mac has broad project access and administrator privileges.

Mitigation: Install only if comfortable granting the service and remote Mac that level of access; review commands before use.

Risk: Project synchronization sends sensitive files, including credentials, by default.

Mitigation: Exclude .env files, private keys, credentials, and tokens with .nomacignore, or use the documented secret-request flow.

Risk: Unpinned agent and MCP packages can change between runs.

Mitigation: Prefer pinned package versions for MCP and agent commands.

Risk: A running cloud Mac retains access and consumes prepaid time.

Mitigation: Stop the Mac when work is complete.

## Reference(s):

- [NoMac skill release](https://clawhub.ai/gergomiklos/skills/nomac)
- [NoMac usage and limits](https://nomac.app/llms.txt)
- [NoMac hosted MCP endpoint](https://mcp.nomac.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide session status, build results, and links for human actions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
