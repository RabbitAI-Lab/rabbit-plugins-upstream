## Description:

查询微信视频号账号的 IP 属地、认证主体、主体类型、服务类别和认证时间等信息。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Users and agents can check a WeChat Video Channel account's published location and certification details when assessing who operates the account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading qhkit and Node tooling can change the host environment.

Mitigation: Review installation steps first; prefer a preinstalled, pinned qhkit version and avoid global installs, runtime package resolution, and shell startup changes.

Risk: Persistently configured Qinghu API tokens may expose credentials on the host.

Mitigation: Use a session-scoped QHKIT_TOKEN instead of storing a token in local configuration.

Risk: Account queries consume Qinghu credits and return third-party account data.

Mitigation: Confirm the estimated charge and user consent before paid calls, and present returned account details with appropriate context.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/autoagc/skills/qinghu-shipinhao-account-info)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise answer or Markdown summary; file export for larger result sets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the account information returned by the service and the credits spent on paid calls.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
