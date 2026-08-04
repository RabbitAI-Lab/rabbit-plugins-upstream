## Description: <br>
Query Huawei Cloud DCS instances, configurations, backups, slow logs, big key and hot key scan tasks, migration tasks, ACL accounts, IP whitelists, tags, quotas, and instance statistics for read-only operations, troubleshooting, and compliance auditing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and compliance reviewers use this skill to inspect Huawei Cloud DCS Redis or Memcached resources and summarize read-only health, performance, backup, migration, access-control, quota, and tag findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud credentials and DCS read access, which can expose operational metadata if credentials are overprivileged or mishandled. <br>
Mitigation: Use a least-privilege read-only IAM policy, avoid pasting real access keys into shared shells or scripts, and rotate credentials as needed. <br>
Risk: Generic Redis requests could be mistaken for Huawei Cloud DCS queries and return cloud-specific guidance in the wrong context. <br>
Mitigation: Confirm that the target resource is Huawei Cloud DCS before using the generated commands or SDK examples. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, Python, and JSON code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Huawei Cloud DCS query guidance with CLI-first commands and Python SDK fallback examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
