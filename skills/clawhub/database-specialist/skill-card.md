## Description: <br>
Database Specialist provides database schema design, SQL optimization, index strategy, migration planning, and performance-diagnosis guidance, with order creation and payment verification handled through a third-party Clawtip service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jinyu12166](https://clawhub.ai/user/jinyu12166) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database engineers, and application teams use this skill to review schema designs, tune SQL queries, plan indexes, assess migrations, and reason about database performance issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends full database question text and encrypted payment credential data to a third-party service. <br>
Mitigation: Install only if this data sharing is acceptable, and avoid including schemas, queries, hostnames, connection strings, secrets, or production details in the question. <br>
Risk: The skill requests network, credential, filesystem read, and filesystem write permissions that are broader than pure database advice requires. <br>
Mitigation: Review why credential access is needed before use, run in a constrained environment when possible, and clean up local order files after verification. <br>
Risk: The service helper script may fail before completing the verification workflow. <br>
Mitigation: Review and test the helper scripts in an isolated environment before relying on the paid service flow. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jinyu12166/skills/database-specialist) <br>
- [Third-party verification service](https://api.ideaidea.com.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown guidance with SQL snippets and helper-script status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a paid verification workflow that writes local order JSON files and exchanges order and credential data with a third-party HTTPS service.] <br>

## Skill Version(s): <br>
1.0.22 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
