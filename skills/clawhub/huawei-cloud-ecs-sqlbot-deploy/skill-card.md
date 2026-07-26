## Description: <br>
Purchase a Huawei Cloud X Instance server and deploy the SQLBot intelligent query application using Python, the Huawei Cloud SDK, and Cloud Operations Center deployment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud engineers use this skill to provision a Huawei Cloud X Instance, configure required networking, and deploy SQLBot after explicit user confirmation. It is intended for users who need a guided SQLBot deployment flow on Huawei Cloud ECS-compatible infrastructure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create paid Huawei Cloud resources and network configuration. <br>
Mitigation: Require explicit user confirmation before creation, review the selected configuration and estimated costs, and release resources after use. <br>
Risk: The skill handles Huawei Cloud credentials and may expose initial passwords in terminal output or optional Feishu messages. <br>
Mitigation: Prefer temporary AK/SK credentials from environment variables, avoid sharing secrets in chat or command history, disable notifications unless needed, and change default server and SQLBot passwords immediately. <br>
Risk: The deployment runs scripts on a newly created server through Huawei Cloud Operations Center. <br>
Mitigation: Review the deployment scripts before execution and scan the created server and exposed services before operational use. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ecs-sqlbot-deploy) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Huawei Cloud X Instance Documentation](https://support.huaweicloud.com/productdesc-flexusx/pd_01_0002.html) <br>
- [Huawei Cloud AK/SK Authentication](https://support.huaweicloud.com/api-iam/iam_01_0001.html) <br>
- [Huawei Cloud Pricing Calculator](https://www.huaweicloud.com/pricing/calculator.html#/hecs) <br>
- [Huawei Cloud Python Package Index](https://repo.huaweicloud.com/repository/pypi/simple) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls] <br>
**Output Format:** [Markdown with inline bash commands and deployment status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Huawei Cloud resource identifiers, public and private IP addresses, service URLs, and initial access credentials that should be rotated immediately.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
