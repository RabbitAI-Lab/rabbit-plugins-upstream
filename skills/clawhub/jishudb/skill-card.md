## Description:

Helps agents install, connect, and troubleshoot JishuDB Desktop and MCP, including service discovery, authorization, and verification through the actual client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to set up or repair a JishuDB Desktop or remote MCP connection, authorize the intended client, and confirm it can use the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Desktop installation downloads and launches an application and may change local client configuration.

Mitigation: Review the version, publisher, app and data paths, client configuration target, MCP URL, and profile in the approval plan before execution; require new approval for changes or retries.

Risk: Credentials or authorization grants could be exposed or applied to the wrong service.

Mitigation: Verify the intended endpoint and actual client connection; complete browser consent or secret entry through the user-facing flow, and never paste tokens into chat.

## Reference(s):

- [JishuDB skill listing](https://clawhub.ai/bowen-aijishu/skills/jishudb)
- [JishuDB skill homepage (listed in metadata)](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/jishudb)
- [Connection recovery](artifact/references/connection-recovery.md)
- [Installation contract](artifact/references/installation-contract.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown text with commands and connection status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports READY, USER_ACTION_REQUIRED, BLOCKED, or FAILED with the next action.]

## Skill Version(s):

0.1.15 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
