## Description:

基于《AI超级个体》帮助用户推进职业转型、专业能力变现、副业验证与一人公司经营。用于 OPC 能力诊断、定位、商业验证、获客交付及行动复盘，按需调用书中 21 个实战模块，并查找菜根智库资料、开展 OPC 市场/案例/政策研究与报告生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[cglt2026opc](https://clawhub.ai/user/cglt2026opc)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this Chinese-language skill to choose and run OPC modules for career diagnosis, capability productization, side-income validation, personal positioning, pricing, content planning, SOP generation, AI team design, resource discovery, research, and action review. The skill produces task-specific guidance and, when requested, reports, plans, scoring inputs, and reusable templates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for sensitive career, income, customer, budget, and business-plan information and can persist reports to local files by default.

Mitigation: Before use, tell the agent not to save or overwrite files unless the path and contents are explicitly approved.

Risk: cgltzk resource suggestions may reflect affiliated resources and public metadata rather than independently verified full-text sources.

Mitigation: Treat cgltzk links as affiliated resource suggestions, verify relevance and access terms before relying on them, and avoid treating metadata as proof that full content was reviewed.

Risk: Some resource downloads require login, membership, payment, CAPTCHA, or other access controls.

Mitigation: Stop automated download attempts when access controls appear; use public metadata or ask the user to download authorized files themselves and provide them to the agent.

## Reference(s):

- [Server-resolved source provenance](https://github.com/cglt2026opc/opc-skills/tree/main/skills/ai-super-individual)
- [ClawHub skill page](https://clawhub.ai/cglt2026opc/skills/ai-super-individual)
- [Download Boundary](references/resources/DOWNLOAD-BOUNDARY.md)
- [Resource Access Contract](references/resources/ACCESS.md)
- [OPC System Research and Report Mode](references/resources/RESEARCH.md)
- [OPC Context](references/resources/OPC-CONTEXT.md)
- [Local cgltzk Resource Snapshot](references/resources/cgltzk-resources.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown responses with optional JSON scoring inputs and outputs, Python command examples, and copied template files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local Markdown reports and copy bundled Word or Excel templates after the user approves the path and contents.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
