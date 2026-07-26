## Description: <br>
社保入税与社保合规专项助手，面向社保费征管划转、缴费基数合规、个税与社保基数匹配、用工分类、历史补缴和社保稽核场景提供结构化自检与实操指引。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, HR and payroll teams, tax practitioners, and business compliance staff use this skill to ask China-focused social-insurance compliance questions, run guided self-checks, and identify records or remediation steps for wage base, individual income tax, labor relationship, flexible work, and audit scenarios. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence rates this release as suspicious because it includes broader tax-service networking, persistent credentials, client configuration hooks, and a bulk skill installer beyond ordinary skill behavior. <br>
Mitigation: Review the skill before installation, confirm that the broader tax-policy cloud service and skill matrix are intended, and install only in an environment where persistent local or browser credentials and remote service calls are acceptable. <br>
Risk: The security guidance warns against use with sensitive payroll, identity, or business compliance data unless data flow and retention terms are clear. <br>
Mitigation: Use anonymized or low-sensitivity inputs until the service endpoint, credential storage, and retention practices have been reviewed and approved. <br>
Risk: Artifact behavior includes configuration hooks and possible skill-directory changes. <br>
Mitigation: Run setup paths in dry-run or a disposable environment first, inspect generated client configuration changes, and keep backups before enabling automatic setup or matrix installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Social insurance workflow page](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with Chinese prose, structured compliance checklists, links, and optional setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct users to a web self-check workflow and remote tax-policy service; users should avoid entering sensitive payroll or identity data unless service terms and data handling are clear.] <br>

## Skill Version(s): <br>
3.14.38 (source: SKILL.md frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
