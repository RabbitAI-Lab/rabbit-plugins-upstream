## Description: <br>
Huawei Cloud DNS Domain Resolution Dynamic Management helps agents manage Huawei Cloud DNS zones and record sets with hcloud CLI, including listing, creating, updating, deleting, validating, and auditing DNS changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to inspect Huawei Cloud DNS zones, manage record sets, perform controlled traffic switches or failovers, validate propagation, and produce DNS change audit logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Huawei Cloud DNS records, including create, update, delete, failover, and traffic-switching operations. <br>
Mitigation: Use a dedicated least-privilege Huawei Cloud IAM user, test in non-production zones first, require explicit human approval for write operations, and use dry-run where supported before applying changes. <br>
Risk: Credential handling may expose Huawei Cloud access keys when environment-variable authentication is passed through command-line parameters. <br>
Mitigation: Prefer interactive hcloud configure, avoid passing AK/SK values as command-line arguments, rotate credentials regularly, and review shell history and process visibility controls. <br>
Risk: The documented pipe-to-bash installer downloads and executes the hcloud CLI installer. <br>
Mitigation: Avoid the pipe-to-bash path unless the installer source is independently verified; install hcloud CLI through a trusted internal process where possible. <br>
Risk: Validation output and audit logs can expose domain names, record values, infrastructure details, and operational timing. <br>
Mitigation: Store audit logs in controlled locations, limit access to validation output, and avoid sharing logs outside the operational team. <br>
Risk: Batch DNS updates are not atomic, so partial changes can remain if one record update fails. <br>
Mitigation: Run dry-run first, validate each affected record after execution, keep a rollback plan, and review the batch summary and audit log for failures. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [DNS API Reference Guide](references/dns-api-guide.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud DNS Documentation](https://support.huaweicloud.com/dns/index.html) <br>
- [KooCLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, JSON examples, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce DNS audit log entries in JSONL, CSV, or JSON when the bundled audit script is used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
