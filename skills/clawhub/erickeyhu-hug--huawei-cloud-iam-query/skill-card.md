## Description: <br>
Queries Huawei Cloud identity and access management resources (IAM) via read-only Python SDK, covering users, groups, policies, agencies, AK/SK, MFA devices, login/password/ACL policies, security compliance, and account quotas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to inspect Huawei Cloud IAM inventory, permissions, credential status, security policies, and account quotas without creating or modifying cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses Huawei Cloud AK/SK credentials. <br>
Mitigation: Run it with least-privilege read-only credentials and avoid exposing credential values in prompts, logs, or shared output. <br>
Risk: The skill creates a local Python environment and installs packages. <br>
Mitigation: Install and run it in an isolated environment after reviewing the dependency installation behavior. <br>
Risk: The skill can print sensitive IAM inventory. <br>
Mitigation: Treat query results as confidential operational data and redact sensitive fields before sharing. <br>
Risk: The security guidance flags network handling, TLS verification, and output-redaction behavior for review. <br>
Mitigation: Use trusted networks and review or patch TLS verification and redaction behavior before operational use. <br>


## Reference(s): <br>
- [IAM Python Script Guide](references/iam/guide.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-iam-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with command examples and JSON or tabular query results from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include sensitive IAM inventory and should be handled as confidential operational data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
