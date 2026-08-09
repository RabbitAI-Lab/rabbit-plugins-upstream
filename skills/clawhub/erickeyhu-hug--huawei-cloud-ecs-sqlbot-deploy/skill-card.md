## Description: <br>
Deploys SQLBot on a Huawei Cloud X instance by guiding credential checks, configuration confirmation, ECS creation, security group setup, EIP binding, and COC-based installation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to provision a Huawei Cloud X instance and deploy SQLBot with guided credential handling, user confirmation, and deployment verification. <br>

### Deployment Geography for Use: <br>
Huawei Cloud regions supported by the skill, including listed regions across China, Asia Pacific, Africa, Latin America, the Middle East, and Turkey. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create billable Huawei Cloud resources. <br>
Mitigation: Use a disposable project or budget-controlled account, require explicit default/custom confirmation before resource creation, and release the server when finished. <br>
Risk: Huawei Cloud AK/SK credentials may be exposed if passed through chat or command-line arguments. <br>
Mitigation: Use temporary, least-privilege credentials through environment variables and avoid entering secrets in conversation or shell history. <br>
Risk: The deployment uses documented default ECS and SQLBot passwords. <br>
Mitigation: Change both the ECS server password and SQLBot admin password immediately after deployment. <br>
Risk: The deployment downloads and executes a remote SQLBot installation script. <br>
Mitigation: Inspect or pin the remote install script before running the deployment in any sensitive environment. <br>
Risk: SQLBot port 8000 may be reachable beyond the intended network scope if security group rules are too broad. <br>
Mitigation: Restrict ingress to trusted IP ranges or internal networks and verify the security group after deployment. <br>
Risk: Optional Feishu notifications may expose deployment details if enabled. <br>
Mitigation: Disable Feishu notifications unless required, and ensure notification content never includes secrets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ecs-sqlbot-deploy) <br>
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Huawei Cloud X Instance Documentation](https://support.huaweicloud.com/productdesc-flexusx/pd_01_0002.html) <br>
- [Huawei Cloud AK/SK Authentication](https://support.huaweicloud.com/api-iam/iam_01_0001.html) <br>
- [Huawei Cloud Price Calculator](https://www.huaweicloud.com/pricing/calculator.html#/hecs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration tables, and deployment result details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Huawei Cloud server identifiers, public and private IP addresses, SQLBot access URL, default credentials that must be changed, and verification steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
