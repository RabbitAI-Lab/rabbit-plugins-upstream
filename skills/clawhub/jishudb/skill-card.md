## Description:

Helps agents install, connect, and troubleshoot JishuDB Desktop or an existing service, including MCP setup and user-operated authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to set up or repair a JishuDB MCP connection, choose a local or remote service, and verify access through their actual client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation downloads and launches a per-user desktop application and changes a client connection entry.

Mitigation: Confirm the JishuDB publisher and review the proposed installation and client changes before approving them.

Risk: OAuth codes or tokens could be exposed if pasted into chat or unprotected configuration.

Mitigation: Complete browser consent or protected token entry in the client; never paste credentials into chat.

## Reference(s):

- [JishuDB skill homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb)
- [Connection recovery](references/connection-recovery.md)
- [Installation contract](references/installation-contract.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports connection status and the next action when setup is incomplete.]

## Skill Version(s):

0.1.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
