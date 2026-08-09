## Description: <br>
Configure passwordless SSH login to Huawei Cloud ECS instances using COC, including IAM agency authorization, SSH key generation, COC script deployment, connection testing, and timed key cleanup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to prepare temporary passwordless SSH access to Huawei Cloud ECS instances through COC while tracking setup, verification, and cleanup steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create privileged SSH access to cloud servers and modify root authorized_keys. <br>
Mitigation: Require explicit approval before execution, prefer a non-root account where feasible, and confirm the target ECS instance and region before running COC commands. <br>
Risk: The workflow keeps an active SSH ControlMaster session after the temporary key is removed. <br>
Mitigation: Review the generated SSH configuration, terminate the ControlMaster session when work is complete, and verify cleanup logs. <br>
Risk: Long-lived AK/SK credentials in shared shells can expose cloud account access. <br>
Mitigation: Avoid persistent AK/SK exports in shared environments and use the shortest practical credential lifetime and session scope. <br>


## Reference(s): <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [IAM Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/intl/en-us/usermanual-hcli/hcli_01_001.html) <br>
- [Huawei Cloud KooCLI Linux Binary](https://hwcloudcli.obs.cn-north-1.myhuaweicloud.com/cli/latest/hcloud_linux_amd64) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and status checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports progress, generated key fingerprints, command strings, COC identifiers, SSH verification results, and cleanup status without exposing private key contents.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
