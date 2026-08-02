## Description: <br>
各类型拟上市与上市公司全生命周期财税顾问与内控框架专项助手，覆盖上市路径论证、上市前财税规范、内控框架、股改涉税、再融资、并购重组、境外架构、持续督导和股权激励场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External company leaders, CFOs, board secretaries, brokers, accountants, tax advisers, and lawyers use this skill to ask Chinese listed-company tax, compliance, internal-control, restructuring, listing-path, and equity-incentive questions. It can also generate self-check guidance, compliance checklists, risk reports, and configuration support for its MCP-backed workflow. <br>

### Deployment Geography for Use: <br>
China and Chinese tax or listing-related cross-border scenarios. <br>

## Known Risks and Mitigations: <br>
Risk: Tax or compliance prompts and self-check metrics may be sent to mcp.aitaxs.top through the cloud MCP workflow. <br>
Mitigation: Use the skill only when that data flow is approved, and avoid submitting confidential company details unless the organization has authorized it. <br>
Risk: Credential and client data may be stored locally in ~/.tax-policy-client and browser localStorage. <br>
Mitigation: Review those storage locations before use in sensitive environments, and clear them when removing or rotating access for the skill. <br>
Risk: Local MCP client configuration can be modified when TAX_ENABLE_AUTOSETUP is intentionally enabled. <br>
Mitigation: Leave auto-setup disabled unless configuration changes are intended, and review any generated MCP configuration before relying on it. <br>
Risk: Search fallback and generated tax guidance may be incomplete or unsuitable for final filing or disclosure decisions. <br>
Mitigation: Validate outputs against authoritative tax, regulatory, accounting, and legal sources before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-listed-advisory) <br>
- [Listed advisory workflow](https://mcp.aitaxs.top/web/topic_workflow_listed_advisory.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain text responses with JSON tool results, HTML workflow output, and Python or shell configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may use a cloud MCP service for policy Q&A, risk checks, calculations, and knowledge-base listings, with local offline reference workflows available when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
