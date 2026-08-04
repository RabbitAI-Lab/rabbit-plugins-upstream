## Description: <br>
Skill specialized for creating buckets on Huawei Cloud OBS. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to prepare and review Huawei Cloud OBS bucket creation commands, validate bucket names, choose regions and storage classes, configure access permissions, and troubleshoot common KooCLI or OBS errors. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce commands that create real Huawei Cloud OBS resources, which may affect cost, quota, and account state. <br>
Mitigation: Require a human review of every bucket name, region, storage class, and ACL before executing generated commands. <br>
Risk: Batch creation may generate multiple buckets and the bundled script assigns public-read ACLs for website or assets purposes. <br>
Mitigation: Avoid batch creation unless the generated names and purposes are understood, and explicitly confirm any public-read ACL before execution. <br>
Risk: The KooCLI installation guide includes remote installer commands and a non-interactive -y variant. <br>
Mitigation: Review the installer source and prefer an interactive installation path before running remote shell commands. <br>
Risk: OBS credentials use AK/SK material that should not be exposed in prompts, logs, or generated commands. <br>
Mitigation: Do not request or display raw AK/SK values; verify credential status without reading or echoing secret configuration files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-obs-bucket-create) <br>
- [KooCLI Installation Guide](references/cli-installation-guide.md) <br>
- [Common Errors and Solutions](references/trouble-shooting.md) <br>
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/cli-koocli/koocli_01_0001.html) <br>
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_002.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Huawei Cloud KooCLI commands, bucket naming checks, ACL and storage-class recommendations, and troubleshooting steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
