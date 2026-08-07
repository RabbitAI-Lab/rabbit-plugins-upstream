## Description: <br>
Create FunctionGraph functions on Huawei Cloud from user-provided function name, runtime, handler, code, memory, timeout, and description parameters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to create, deploy, or upload Huawei Cloud FunctionGraph serverless functions without manual console work. It supports CLI-driven function creation and verification workflows for development, batch creation, workflow deployment, and CI/CD integration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or change Huawei Cloud FunctionGraph resources and may incur cost or expose functions if used against the wrong project, region, name, or trigger. <br>
Mitigation: Use a sandbox or least-privilege Huawei Cloud account, verify the region, project, resource name, and trigger settings before each action, and remove test functions or API triggers after verification. <br>
Risk: Huawei Cloud AK/SK credentials are required and could be exposed through conversation, logs, code, or command history. <br>
Mitigation: Provide credentials only through environment variables or approved local configuration, never paste AK/SK values into conversation, code, or logs, and prefer an IAM user with minimal permissions. <br>
Risk: Broad wildcard IAM policies in examples can grant more cloud permissions than this function creation workflow needs. <br>
Mitigation: Prefer the minimum required or resource-specific IAM policy, avoid broad wildcard actions, and review cross-service permissions before enabling OBS, VPC, APIG, DIS, or LTS integrations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-functiongraph-function-create) <br>
- [FunctionGraph Documentation](https://support.huaweicloud.com/functiongraph/) <br>
- [Huawei Cloud FunctionGraph Product Documentation](https://support.huaweicloud.com/productdesc-functiongraph/index.html) <br>
- [Huawei Cloud Python SDK v3](https://github.com/huaweicloud/huaweicloud-sdk-python-v3) <br>
- [Huawei Cloud Python SDK](https://github.com/huaweicloud/huaweicloud-sdk-python) <br>
- [IAM Policies Guide](references/iam-policies.md) <br>
- [SDK Installation Guide](references/sdk-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or verifies Huawei Cloud FunctionGraph resources using configured Huawei Cloud credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
