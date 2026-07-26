## Description: <br>
Huawei Cloud EIP Cost Optimizer helps agents use hcloud CLI shell scripts to list EIPs, detect idle or unbound addresses, estimate costs, generate reports, configure alerts, and keep audit logs without releasing or deleting resources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, cloud operators, and FinOps teams use this skill to inspect Huawei Cloud EIP inventory, identify idle or unbound EIPs, estimate avoidable costs, generate reports, configure monitoring alerts, and maintain audit records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes local installation and dependency-fix paths. <br>
Mitigation: Review installer and --fix commands before running them, and install hcloud CLI, jq, bc, and curl from approved internal sources where required. <br>
Risk: Monitoring setup can create cron persistence. <br>
Mitigation: Review the crontab entry before enabling monitoring, and use the documented removal command when scheduled checks are no longer needed. <br>
Risk: Webhook or email alerts can disclose public IP addresses and EIP identifiers. <br>
Mitigation: Send alerts only to approved HTTPS webhook domains and internal email destinations. <br>
Risk: The skill requires Huawei Cloud credentials for inventory and reporting. <br>
Mitigation: Use least-privilege read-only IAM credentials, avoid command-line credential arguments, and prefer temporary credentials when available. <br>
Risk: Cost reports are estimates because the API does not expose charge_mode. <br>
Mitigation: Treat savings values as planning guidance and confirm billing impact in Huawei Cloud billing data before taking action. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [EIP API Guide](references/eip-api-guide.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [KooCLI Official Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [KooCLI Reference](https://support.huaweicloud.com/cli/reference.html) <br>
- [Huawei Cloud EIP Documentation](https://support.huaweicloud.com/eip/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>
- [IAM AK/SK Management](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts can produce text, HTML, JSON, JSONL, and CSV outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Cost estimates depend on regional pricing assumptions and API-visible EIP metadata; monitoring alerts can include public IP and EIP identifiers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
