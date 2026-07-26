## Description: <br>
Routes code-generation requests through the Huawei Cloud CodeArts CLI so CodeArts can generate code and return structured results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to send structured implementation requests to Huawei Cloud CodeArts, configure required credentials and permissions, and run CodeArts code generation through its CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide Huawei Cloud AK/SK credentials and can store them in plaintext shell environment configuration. <br>
Mitigation: Use temporary, least-privilege credentials and delete CODEARTS_CLI_AK and CODEARTS_CLI_SK from shell startup files after use. <br>
Risk: The setup flow downloads and executes a remote CodeArts installer script. <br>
Mitigation: Review the downloaded installer source and run the setup only in a controlled environment where remote installer execution is acceptable. <br>
Risk: The permission setup can grant broad local file read/write or web capabilities. <br>
Mitigation: Inspect the generated permission file and restrict permissions to the active workspace instead of granting global access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-codearts-code-gen) <br>
- [Huawei Cloud access key documentation](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html) <br>
- [Huawei Cloud IAM access key console](https://console.huaweicloud.com/iam/?#/mine/accessKey) <br>
- [CodeArts CLI Linux and macOS installer](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.sh) <br>
- [CodeArts CLI PowerShell installer](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON CLI status responses and generated code files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify local project files through CodeArts CLI after credentials and file-permission consent.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
