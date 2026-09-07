## Description:

指导 agent 规范操作 GBrain 本地知识库（经 MCP 接入 WorkBuddy）。涵盖 GBrain 概念与安装形态、分类规范（路径前缀→类型）、资料入库、链接/标签关联、schema pack 切换、健康度治理、100G 大库分批处理与 Obsidian 联动。当涉及"把资料存进 GBrain / 用 GBrain 检索 / 整理知识库 / gbrain MCP 调用"时加载。

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide an agent in organizing, importing, searching, linking, and maintaining a local GBrain knowledge base through WorkBuddy MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to reorganize and ingest large local document sets, which may affect local files or expose content to cloud processing.

Mitigation: Require explicit approval before file moves, imports, batch ingestion, or cloud API processing, and start with small batches that can be reviewed.

Risk: The skill includes guidance for hidden Windows startup persistence, watchdog behavior, and working around WorkBuddy execution safeguards.

Mitigation: Remove or ignore hidden VBS startup/watchdog and safeguard-bypass guidance before deployment, and require explicit approval for service startup changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/gbrain-guide)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and MCP tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file organization, GBrain imports, MCP calls, and Windows service-management steps.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
