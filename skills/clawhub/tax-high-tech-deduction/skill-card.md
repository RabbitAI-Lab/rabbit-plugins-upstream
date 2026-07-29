## Description: <br>
Helps agents guide high-tech enterprise certification and R&D super-deduction compliance, including eligibility checks, expense categorization, risk self-checks, evidence-chain summaries, and multi-basis R&D reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users use this skill to assess high-tech enterprise qualification, R&D expense super-deduction treatment, supporting records, and related audit readiness. Agents can use it to produce structured guidance, calculations, checklists, reports, configuration snippets, and offline fallback references. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Questions, risk scenarios, web self-check metrics, or sensitive tax and R&D details may be sent to the vendor's remote service. <br>
Mitigation: Use only approved data in enterprise or advisory environments, avoid confidential payroll, R&D, audit, or tax-return details unless approved, and prefer offline reference workflows for low-sensitivity checks when remote use is not approved. <br>
Risk: Optional MCP setup can change local client configuration when automatic setup is enabled. <br>
Mitigation: Check whether TAX_ENABLE_AUTOSETUP is set before running configuration scripts, review proposed MCP configuration changes, and keep backups of affected client config files. <br>
Risk: Credentials, logs, or web self-check data may persist locally. <br>
Mitigation: Review and clean ~/.tax-policy-client and browser localStorage according to the user's data-retention policy, especially after handling regulated tax or audit information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [High-tech tax workflow page](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [National Taxation Administration](https://www.chinatax.gov.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code snippets, shell commands, configuration snippets, tool-call text, and CSV-exportable web self-check results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide online MCP-backed answers when remote service use is enabled and offline reference guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
