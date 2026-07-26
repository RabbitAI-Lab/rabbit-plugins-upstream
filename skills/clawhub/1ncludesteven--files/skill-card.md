## Description: <br>
Skill to call Cloud API for Tencent Cloud (腾讯云). Used for cloud automation or resource management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[1ncludesteven](https://clawhub.ai/user/1ncludesteven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to guide Tencent Cloud API work through tccli, including authentication, service discovery, read-only queries, and resource-management commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is presented with file-utility metadata while the skill guides Tencent Cloud authentication and resource-management commands. <br>
Mitigation: Install and use it only when Tencent Cloud administration is intended, and make the cloud-management scope clear to reviewers and operators before use. <br>
Risk: Some generated tccli commands may create or change cloud resources. <br>
Mitigation: Require explicit user confirmation before any non-read-only command and review command parameters, target account, and region before execution. <br>
Risk: Credential exposure could occur if commands print or request Tencent Cloud secrets. <br>
Mitigation: Use browser-based tccli auth login and avoid commands that request, print, or list SecretId or SecretKey values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/1ncludesteven/skills/files) <br>
- [Configure TCCLI credentials](references/auth.md) <br>
- [Install TCCLI](references/install.md) <br>
- [Information retrieval steps and examples](references/refs.md) <br>
- [Tencent Cloud API service index](https://cloudcache.tencentcs.com/capi/refs/services.md) <br>
- [TencentCloud CLI repository](https://github.com/TencentCloud/tencentcloud-cli.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include tccli and curl commands that require user review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
