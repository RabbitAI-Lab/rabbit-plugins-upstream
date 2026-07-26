## Description: <br>
Query and manage Salesforce CRM data via the Salesforce CLI (`sf`), including SOQL/SOSL queries, schema inspection, record changes, bulk operations, Apex execution, metadata deployment, and raw REST API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arvorco](https://clawhub.ai/user/arvorco) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, Salesforce administrators, and operators use this skill to query CRM data, inspect schemas, manage records, run bulk operations, execute Apex, deploy metadata, and call Salesforce APIs through the Salesforce CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority to read from and change Salesforce org data. <br>
Mitigation: Install only from a trusted publisher, use least-privileged Salesforce users and sandbox orgs where practical, and require explicit confirmation before record changes, Apex execution, raw API calls, or bulk data operations. <br>
Risk: Salesforce authentication output can expose tokens, auth URLs, instance/session details, or private key paths. <br>
Mitigation: Do not print, save, or summarize raw authentication output; redact sensitive values before sharing or storing command results. <br>


## Reference(s): <br>
- [Salesforce CLI](https://developer.salesforce.com/tools/salesforcecli) <br>
- [ClawHub Salesforce Skill](https://clawhub.ai/arvorco/skills/salesforce) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline Salesforce CLI commands, JSON-oriented command output expectations, and code blocks for SOQL, SOSL, Apex, REST request bodies, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the Salesforce CLI (`sf`) and an authenticated Salesforce org before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
