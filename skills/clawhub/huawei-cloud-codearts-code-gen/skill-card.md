## Description:

Routes code-generation requests through the Huawei Cloud CodeArts CLI so CodeArts can generate code from structured task descriptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to route implementation requests to Huawei Cloud CodeArts for code generation after environment, credential, permission, and connection checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes broad coding requests through an external CodeArts CLI and external task processing.

Mitigation: Install only when that routing is intentional, and avoid sending sensitive code or requirements unless external processing is approved.

Risk: The setup flow downloads and executes a remote installer.

Mitigation: Prefer a scoped release that verifies installer integrity and review the installer source before deployment.

Risk: Huawei Cloud AK/SK credentials may be persisted in plaintext local environment configuration.

Mitigation: Use session-only credentials or a secure credential store where possible, and remove stored credentials after use.

Risk: The permission helper can grant broad local edit and write access to the CodeArts CLI.

Mitigation: Restrict permissions to the active workspace and review generated file changes before accepting them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-codearts-code-gen)
- [Huawei Cloud IAM access key documentation](https://support.huaweicloud.com/usermanual-iam/iam_02_0003.html)
- [Huawei Cloud IAM access key console](https://console.huaweicloud.com/iam/?#/mine/accessKey)
- [CodeArts CLI Linux and macOS installer](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.sh)
- [CodeArts CLI Windows installer](https://cnnorth4-cloudide-marketplace.obs.cn-north-4.myhuaweicloud.com/codearts/cli_tui/install_script/install.ps1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON status messages and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Huawei Cloud AK/SK credentials and user consent for local file permissions before CodeArts code generation.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
