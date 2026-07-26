## Description: <br>
Manage Salesforce CRM records through the Salesforce CLI or REST API, including querying, creating, updating, deleting, and bulk operations for common CRM objects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lucas-riverbi](https://clawhub.ai/user/lucas-riverbi) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Sales, support, RevOps, and CRM administrators can use this skill to inspect Salesforce data, manage contacts, accounts, opportunities, leads, cases, and tasks, and prepare CLI or REST workflows for routine CRM operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Salesforce permissions could expose or alter sensitive CRM records across contacts, accounts, opportunities, leads, cases, and tasks. <br>
Mitigation: Use a least-privilege Salesforce account, test in a sandbox first, and require human approval before production updates, deletes, imports, exports, or arbitrary SOQL queries. <br>
Risk: Access tokens and command output may contain sensitive customer or business data. <br>
Mitigation: Treat Salesforce tokens as secrets and avoid sharing or persisting command output in logs that are visible to unauthorized users. <br>


## Reference(s): <br>
- [Salesforce CLI](https://developer.salesforce.com/tools/salesforcecli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash, SOQL, JSON, and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Salesforce CLI or REST commands that read or modify CRM data; requires Salesforce authentication and a target org.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
