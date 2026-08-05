## Description: <br>
Routes code generation requests through the Huawei Cloud CodeArts CLI, including setup checks, credential prompts, permission configuration, and result reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to delegate implementation tasks to Huawei Cloud CodeArts through the CodeArts CLI. It guides environment setup, access-key collection, workspace permission authorization, model selection, and generated-result reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Huawei Cloud access keys may be persisted in plaintext shell or user environment storage. <br>
Mitigation: Use a narrowly scoped or temporary access key when possible, avoid saving secrets when not needed, and delete stored CODEARTS_CLI_AK and CODEARTS_CLI_SK values after use. <br>
Risk: Setup downloads and executes a remote CodeArts CLI installer. <br>
Mitigation: Install only when CodeArts routing is intended and inspect the remote installer source before executing it. <br>
Risk: Permission setup can grant broad local file read/write access. <br>
Mitigation: Restrict CodeArts permissions to the active workspace instead of allowing global access. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-codearts-code-gen) <br>
- [Huawei Cloud IAM access key documentation](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html) <br>
- [Huawei Cloud IAM access key console](https://console.huaweicloud.com/iam/?#/mine/accessKey) <br>
- [CodeArts CLI Linux/macOS installer source](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.sh) <br>
- [CodeArts CLI PowerShell installer source](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON status payloads, shell and PowerShell commands, and CodeArts-generated code or files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK credentials and explicit local file-permission authorization before generation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
