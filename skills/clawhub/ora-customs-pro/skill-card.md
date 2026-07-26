## Description: <br>
海关数据分析专家Skill — 海关查询系统，海关数据查询平台，海关数据分析，海关数据统计，全球海关数据查询，外贸数据，国外进出口数据，提单数据，关单数据，国外采购商平台，海关数据查询，全球进出口数据，中国进出口数据，找国外客户，国外采购商订单。支持按HS编码/产品名称、采购商、供应商进行多维度贸易数据分析 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oraagent](https://clawhub.ai/user/oraagent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade analysts, sales teams, and sourcing teams use this skill to query and analyze customs import/export data by HS code or product, buyer, supplier, country, time trend, recent records, trade intelligence, and shipping details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses an API key locally. <br>
Mitigation: Use a dedicated, low-privilege key, rotate it if exposed, and control file permissions in shared workspaces. <br>
Risk: Queries and credentials are sent to the customs query service. <br>
Mitigation: Install only if you trust the service and avoid entering sensitive or confidential trade terms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oraagent/skills/ora-customs-pro) <br>
- [OraAgent publisher profile](https://clawhub.ai/user/oraagent) <br>
- [Topeasy China homepage](https://www.topeasychina.com) <br>
- [Customs query service endpoint](https://h.smtso.com/skill/botcustoms) <br>
- [Ora service information](https://www.oraskl.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON API results summarized for the user] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke a Node.js client that returns JSON from the customs query service.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
