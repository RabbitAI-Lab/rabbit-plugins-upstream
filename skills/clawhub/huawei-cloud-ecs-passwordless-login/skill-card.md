## Description: <br>
Configure passwordless SSH login to Huawei Cloud ECS instances using COC by automating IAM agency authorization, SSH key generation, COC script deployment, SSH connection testing, and timed key cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to set up short-lived passwordless SSH access to Huawei Cloud ECS instances through COC, verify connectivity, and clean up deployed keys after the workflow completes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill creates temporary root SSH credentials and may preserve active SSH access after key cleanup through ControlMaster. <br>
Mitigation: Require explicit opt-in for ControlMaster persistence, prefer a least-privileged SSH user where possible, keep ControlPersist short, and verify remote authorized_keys cleanup succeeds. <br>
Risk: The workflow changes local SSH behavior by appending an SSH config entry and creating a ControlMaster socket. <br>
Mitigation: Review the SSH config entry before use, remove the entry and socket after the session is no longer needed, and keep persistence settings aligned with the operational need. <br>
Risk: Huawei Cloud AK/SK credentials and generated private keys could be exposed through shared shells, logs, or agent output. <br>
Mitigation: Avoid shared shell history and logs, never print private key content, store keys only in the temporary location for the cleanup window, and confirm local key deletion. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/intl/en-us/usermanual-hcli/hcli_01_001.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured Markdown progress reports with inline shell commands, JSON command files, SSH configuration snippets, status values, and cleanup guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses ECS instance or IP, region, SSH user, cleanup delay, and ControlPersist timeout; creates temporary SSH keys and COC JSON files during execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
