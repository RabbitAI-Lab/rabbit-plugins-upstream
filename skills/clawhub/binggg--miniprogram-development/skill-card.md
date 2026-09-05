## Description:

Supports agents developing WeChat Mini Programs with project structure, debugging, preview and upload workflows, CloudBase integration, message push, customer service, and WeChat search optimization guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modify, debug, preview, upload, publish, and optimize WeChat Mini Program projects, including projects that explicitly use CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned CLI or MCP package commands can create supply-chain drift across production or CI runs.

Mitigation: Review or pin npx and MCP package versions before using the skill in production or CI.

Risk: Preview, upload, deploy, and cloud write actions can affect WeChat Mini Program or CloudBase resources.

Mitigation: Confirm the target project, appid, CloudBase environment, and intended operation before allowing those actions to run.

Risk: The skill may require agent access to local project files, WeChat Developer Tools, and CloudBase workflows.

Mitigation: Install and use it only for WeChat Mini Program workspaces where that level of access is expected.

## Reference(s):

- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](artifact/references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](artifact/references/seo-search-optimization.md)
- [WeChat IDE Skills vs CloudBase MCP](artifact/references/wxide-vs-cloudbase-mcp.md)
- [Common Pitfalls](artifact/references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, JSON, XML, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits, preview or upload commands, and configuration changes for WeChat Mini Program projects.]

## Skill Version(s):

1.28.47 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
