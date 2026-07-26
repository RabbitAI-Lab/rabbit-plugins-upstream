## Description: <br>
Skill specialized for creating buckets on Huawei Cloud OBS, including bucket property setup, access permission configuration, and guidance for bucket creation workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to create Huawei Cloud OBS buckets, validate bucket names, choose regions and storage classes, configure ACLs, and troubleshoot common creation failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help create Huawei Cloud OBS resources, including buckets with public-read access. <br>
Mitigation: Review generated commands before execution, prefer private ACLs, and require explicit user approval before creating any public bucket. <br>
Risk: The installation guidance includes remote KooCLI installer commands. <br>
Mitigation: Verify the installer source and contents before running downloaded shell scripts. <br>
Risk: Credential handling mistakes could expose Huawei Cloud AK/SK secrets. <br>
Mitigation: Do not paste secrets into chat, do not read local credential files into the agent context, and use credential status checks that avoid revealing secret values. <br>


## Reference(s): <br>
- [KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Common Errors and Solutions](references/trouble-shooting.md) <br>
- [Huawei Cloud KooCLI Preparation](https://support.huaweicloud.com/qs-hcli/hcli_02_002.html) <br>
- [Huawei Cloud KooCLI Documentation](https://support.huaweicloud.com/cli-koocli/koocli_01_0001.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include Huawei Cloud OBS CLI commands for bucket creation, validation, listing, and property inspection.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
