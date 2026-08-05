## Description:

WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, preview, publish, and optimize WeChat Mini Program projects, including pages, components, routing, tabBar setup, project configuration, assets, and release workflows. It also guides CloudBase integration when a mini program project explicitly uses wx.cloud, Tencent CloudBase, or related CloudBase features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through WeChat DevTools preview/upload flows and authenticated CloudBase operations.

Mitigation: Review and approve publish, upload, cloud write, and authenticated operations before execution.

Risk: Mini Program projects can fail when project configuration, appid, environment ID, or local assets do not match the actual project state.

Mitigation: Confirm project.config.json, miniprogramRoot, appid, CloudBase environment, and referenced assets before previewing, uploading, or changing cloud resources.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Common Pitfalls in WeChat Mini Program Development](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project checks, preview or upload steps, CloudBase guidance, and Mini Program file examples.]

## Skill Version(s):

1.28.26 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
