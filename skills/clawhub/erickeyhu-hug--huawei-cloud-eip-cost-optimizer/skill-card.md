## Description: <br>
Analyzes Huawei Cloud Elastic IP inventory with hcloud CLI to identify idle or unbound EIPs, estimate costs, generate reports, configure alerts, and maintain audit logs without releasing or modifying EIPs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Cloud operations and FinOps engineers use this skill to inspect Huawei Cloud EIPs across regions, find idle or unbound addresses, estimate avoidable costs, configure monitoring alerts, and document audit activity while leaving destructive release decisions manual. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shell-based dependency setup can execute an external hcloud installer or package-manager commands when automatic fixes are requested. <br>
Mitigation: Review installer contents and run dependency installation manually on sensitive hosts; avoid the --fix path unless the execution environment is trusted. <br>
Risk: Environment-variable credentials may be exposed through command-line arguments or process inspection. <br>
Mitigation: Prefer interactive hcloud configure storage, avoid echoing secrets, and use least-privilege IAM credentials for the read-only EIP permissions described in the policy reference. <br>
Risk: Monitoring setup can persist a daily cron job and continue querying cloud inventory after initial use. <br>
Mitigation: Review the cron entry before enabling monitoring and remove it with the provided remove option when ongoing checks are no longer needed. <br>
Risk: Webhook or email alerts can share EIP IDs and public IP addresses outside the local environment. <br>
Mitigation: Send alerts only to trusted HTTPS webhook destinations or trusted mail systems approved to receive infrastructure inventory details. <br>
Risk: Cost recommendations are estimates because the EIP API does not expose billing charge mode and EIP release is irreversible. <br>
Mitigation: Validate costs against Huawei Cloud billing data and confirm business ownership before manually releasing or resizing any EIP. <br>


## Reference(s): <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [EIP API Guide](references/eip-api-guide.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud CLI documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud CLI reference](https://support.huaweicloud.com/cli/reference.html) <br>
- [Huawei Cloud IAM user guide](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, HTML, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands plus script-generated text, JSON, HTML, JSONL, and CSV reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only hcloud CLI analysis; reports, audit logs, cron entries, and alert messages may be produced when the corresponding script options are used.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
