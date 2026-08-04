## Description: <br>
国内电商平台、直播带货、MCN、主播和平台报送场景的财税合规专题助手，提供政策问答、风险自查、案例分析、报告模板和实操指引。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business users, tax professionals, platform merchants, livestream teams, and agent developers use this skill to ask ecommerce and livestream tax-compliance questions, run lightweight self-checks, identify invoice and private-account collection risks, and draft practical remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send tax questions and self-check data to a remote cloud service. <br>
Mitigation: Review the configured service endpoint before use and avoid entering taxpayer IDs, account numbers, invoice details, or confidential business facts unless that data handling is approved. <br>
Risk: The skill can store local credentials, cache files, and logs under ~/.tax-policy-client. <br>
Mitigation: Inspect and protect the local data directory, remove stale credentials or logs when no longer needed, and apply local access controls appropriate for tax-related data. <br>
Risk: The skill can modify local MCP or client configuration when auto-setup is enabled. <br>
Mitigation: Run setup in dry-run mode first, review any proposed Claude/Cursor/Cline configuration entries and backups, and only enable write mode after approving the change. <br>
Risk: Tax calculations and policy guidance may be incomplete or time-sensitive. <br>
Mitigation: Treat outputs as advisory, confirm current rules with official tax authority sources or qualified professionals, and do not use the skill as a substitute for filing, audit, or legal representation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Ecommerce compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [National Taxation Administration website](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown text, JSON-like tool responses, Python code, shell commands, configuration snippets, and local HTML workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce advisory tax-compliance answers, self-check findings, calculation results, remediation checklists, report drafts, and local setup guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
