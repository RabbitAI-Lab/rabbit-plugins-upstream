## Description: <br>
该技能帮助用户在投资、合作、并购或签约前，基于公开招投标数据生成企业经营实态尽调报告，覆盖中标流水、订单趋势、客户结构、履约能力、竞对和公开风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, investors, procurement teams, and business development teams use this skill to evaluate a company's operating reality before investment, partnership, acquisition, supplier selection, or contract signing. It produces single-company due diligence reports and two-company comparison reports using tender and bidding records, public risk checks, and clearly stated data boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The vendor may receive company queries and, during auto-registration, a hashed device identifier. <br>
Mitigation: Install only if you trust the publisher; prefer setting ZLBX_API_KEY manually and use auto-registration only after explicit consent. <br>
Risk: Persistent credentials and signed login-bypass links are sensitive. <br>
Mitigation: Protect local credential files, avoid sharing generated sk or auto-login links, and rotate credentials if exposed. <br>
Risk: Reports and optional HTML files can contain business-sensitive due diligence findings, contact data, and signed links. <br>
Mitigation: Review reports before forwarding, request contact data only for a legitimate business reason, and keep shared files within the intended audience. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bidding-due-diligence) <br>
- [API quick reference](references/api-quick.md) <br>
- [Enterprise intelligence workflow](references/workflow.md) <br>
- [Report template](references/report-template.md) <br>
- [Auto-registration flow](references/auto-register.md) <br>
- [知了商机大师](https://agent.zhiliaobiaoxun.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown reports in chat, with optional local HTML report files generated from structured report data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based account setup; may use vendor APIs, WebSearch, local credential storage, and local report files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
