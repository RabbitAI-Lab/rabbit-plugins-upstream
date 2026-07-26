## Description: <br>
对企业或组织进行合规的外贸客户开发与决策人信息查询，仅在用户明确授权并符合当地隐私、反垃圾和商业通信法规的前提下使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oraagent](https://clawhub.ai/user/oraagent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business development teams use this skill to look up company details and decision-maker contact signals by company name, domain, or LinkedIn company identifier after confirming authorization and compliance requirements. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries and authorization derived from OraAgent.key are sent to the external Ora/Topeasy API. <br>
Mitigation: Use the skill only for authorized business contact lookup and confirm the user accepts the external data processing before running a search. <br>
Risk: Generated temporary JSON result files may contain company or personal contact details. <br>
Mitigation: Treat result files as sensitive, share only necessary fields, and remove temporary files when they are no longer needed. <br>
Risk: Returned decision-maker or contact information could be misused for unauthorized collection or harassing marketing. <br>
Mitigation: Stop when authorization or compliance is unclear, and do not use the skill for privacy-invasive or unlawful outreach scenarios. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oraagent/skills/ora-contact-pro) <br>
- [Publisher profile](https://clawhub.ai/user/oraagent) <br>
- [Topeasy API service endpoint](https://api.topeasychina.com:6443/TPAiAgentSkill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON files, Guidance] <br>
**Output Format:** [Markdown summary with referenced JSON result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads OraAgent.key, queries an external Ora/Topeasy API, and stores raw JSON results under the system temporary directory.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
