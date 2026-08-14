## Description:

企业专利管理系统构建助手 —— 基于智慧芽 PatSnap API，为合成生物学/生命科学企业自动构建完整专利管理系统，输出单文件 HTML 可视化系统。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP teams, patent managers, and developers at synthetic biology or life science companies use this skill to build or update a patent management dashboard from PatSnap/智慧芽 patent data. It guides an agent through patent sync, asset tracking, fee alerts, competitor monitoring, FTO analysis, value scoring, novelty search, and single-file HTML output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill retrieves patent records through configured PatSnap/智慧芽 MCP access and can update a local HTML dashboard for enterprise IP workflows.

Mitigation: Confirm the target company, authorization scope, and whether the user wants read-only analysis or local HTML updates before running data-sync prompts.

Risk: Without PatSnap/智慧芽 MCP configuration, the skill cannot retrieve live patent data or generate database-backed conclusions.

Mitigation: Treat output as framework or analysis guidance until the user has completed account authorization and enabled the required MCP tools.

## Reference(s):

- [PatSnap/智慧芽 Open Platform](https://open.zhihuiya.com/)
- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-management-system)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions and generated single-file HTML code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected output is a UTF-8 patent_v{n}.html dashboard saved under @session/scripts/ when the agent has the required PatSnap/智慧芽 MCP access.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
