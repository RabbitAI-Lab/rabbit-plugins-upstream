## Description: <br>
各类型拟上市与上市公司全生命周期财税顾问与内控框架专项助手，覆盖上市路径论证、上市前财税规范、内控框架设计、股改涉税、再融资、并购重组、境外架构、持续督导和股权激励。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External company leaders, board secretaries, CFOs, and their securities, accounting, tax, and legal advisers use this skill to assess listing paths, tax cleanup, internal controls, restructuring, overseas structures, ongoing compliance, and equity incentive tax issues. It can produce policy-oriented Q&A, risk self-checks, remediation guidance, and compliance report drafts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions, risk scenarios, and advisory context to remote services. <br>
Mitigation: Use it only with organizational approval for that data flow, and avoid entering confidential company, IPO, ownership, tax, or internal-control details unless approved. <br>
Risk: The skill registers and stores local credentials and logs for cloud-backed service access. <br>
Mitigation: Review local credential and log handling before deployment, and rotate or remove local credentials when the skill is no longer authorized. <br>
Risk: Setup behavior can alter MCP client configuration when explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode until configuration changes are reviewed, and rely on backups before enabling automatic writes. <br>
Risk: Tax and internal-control outputs may be incomplete or unsuitable for regulated filing, audit, or legal decisions. <br>
Mitigation: Treat generated guidance and report drafts as review material, and validate conclusions with qualified tax, audit, legal, or compliance professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-listed-advisory) <br>
- [zxj2devs publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [上市业务财税合规自检页面](https://mcp.aitaxs.top/web/topic_workflow_listed_advisory.html) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text, with optional report-style content, code snippets, shell commands, and MCP configuration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a cloud-backed tax MCP service and local/offline fallback utilities.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
