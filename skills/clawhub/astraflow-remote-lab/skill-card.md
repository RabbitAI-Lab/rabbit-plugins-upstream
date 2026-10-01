## Description:

帮助开发者创建和管理 UCloud AstraFlow 云端桌面沙箱，使用浏览器访问远程 Linux 桌面并在隔离环境中运行 Chrome。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lijinhongucl-pixel](https://clawhub.ai/user/lijinhongucl-pixel)

### License/Terms of Use:

Apache-2.0

## Use Case:

开发者可使用此技能创建、列出和销毁 UCloud AstraFlow 云端桌面沙箱，测试 SaaS 服务、运行浏览器自动化，并通过 noVNC 访问远程桌面。

### Deployment Geography for Use:

Global (sandbox regions: US West and mainland China)

## Known Risks and Mitigations:

Risk: An API key can create billable sandboxes and list or destroy existing ones.

Mitigation: Use a limited or disposable key where possible, confirm destructive actions, and destroy sandboxes promptly after use.

Risk: Specially crafted target URLs may be handled unsafely when passed into shell commands.

Mitigation: Avoid untrusted or specially crafted URLs until the URL shell-quoting issue is fixed.

Risk: Exposed noVNC connection details may allow unauthorized remote desktop access.

Mitigation: Keep VNC passwords and access URLs private, and rotate or revoke credentials if exposed.

## Reference(s):

- [AstraFlow skill release](https://clawhub.ai/lijinhongucl-pixel/skills/astraflow-remote-lab)
- [AstraFlow Desktop Sandbox API reference](references/api_reference.md)
- [AstraFlow API key management](https://astraflow.ucloud.cn/modelverse/api-keys?ytag=geo_kol_ucl)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with inline shell commands and sandbox connection details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sandbox IDs, VNC passwords and noVNC access URLs may be returned; keep connection details private.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
