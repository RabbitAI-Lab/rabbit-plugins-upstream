## Description:

Helps agents build, debug, preview, publish, optimize, and operate WeChat Mini Program projects, including CloudBase integration, WeChat Developer Tools workflows, message push, customer-service replies, and WeChat search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modify, debug, preview, upload, publish, and optimize WeChat Mini Program projects. It also guides CloudBase-specific mini program work when the project explicitly uses wx.cloud, Tencent CloudBase, message push, customer-service replies, or WeChat search indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cloud deployment, upload, message-push, and customer-service workflows can affect real cloud resources or user-facing mini program behavior.

Mitigation: Review and approve deployment, upload, message-push binding, customer-service reply, and MCP authentication actions before execution.

Risk: Incorrect CloudBase assumptions can lead to web-style authentication, wrong environment IDs, or writes against the wrong project.

Mitigation: Confirm the project uses CloudBase, read project.config.json, verify appid and environment details, and use wx.cloud mini program patterns only when applicable.

Risk: Message-push and customer-service reply setup can silently fail if undocumented bypasses, missing OpenAPI permissions, or omitted remote npm installation are used.

Mitigation: Use the documented IDE or wxide path, declare customerServiceMessage.send permission, deploy receiver functions with remote npm installation, and validate through IDE cloud-function logs.

Risk: Preview or upload commands can publish unintended behavior if project configuration or release gates are skipped.

Mitigation: Check miniprogramRoot, appid, referenced assets, and deployment gate requirements before previewing, uploading, or publishing.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Message Push & Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO & WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program Search Optimization](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [WeChat Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project file edits, configuration checks, deployment steps, preview/upload commands, and troubleshooting guidance.]

## Skill Version(s):

1.28.39 (source: server release metadata; artifact frontmatter reports 2.32.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
