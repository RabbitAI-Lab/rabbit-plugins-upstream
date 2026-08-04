## Description: <br>
Lists Huawei Cloud Virtual Private Clouds for the current tenant or project, including key metadata, optional filters, pagination, and read-only CLI or SDK fallback paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and network engineers use this skill to inspect Huawei Cloud VPC inventory for planning, troubleshooting, and enterprise-project audits without changing cloud resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Huawei Cloud authentication and may need access to cloud account configuration. <br>
Mitigation: Use a least-privilege read-only IAM policy and configure credentials outside the chat session. <br>
Risk: Using all_granted_eps can expose VPC metadata across every enterprise project the account can access. <br>
Mitigation: Use project-specific filters when broad enterprise-project visibility is unnecessary. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-vpc-list) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Data Flow Diagram](references/dataflow-diagram.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI Download](https://obs-community-tool.obs.cn-north-1.myhuaweicloud.com/hcloudcli/latest/hcloudcli-linux-amd64.tar.gz) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown with inline shell commands and summarized VPC metadata] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns read-only VPC inventory details such as id, name, CIDR, status, description, and enterprise project.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
