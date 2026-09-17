## Description:

Helps coding agents build, debug, preview, publish, optimize, and integrate CloudBase-backed WeChat Mini Program projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modify, debug, preview, deploy, publish, and promote WeChat Mini Programs. It is especially useful when coordinating project configuration, WeChat Developer Tools workflows, CloudBase integration, message push, customer-service replies, and search indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Documented npx commands may execute remote packages without pinned versions.

Mitigation: Pin npm packages or verify package versions before running commands, and avoid automatic skill installs with -y unless the source is already trusted.

Risk: Sample logging patterns may retain customer message data, media references, tokens, or raw OpenIDs.

Mitigation: Redact message bodies, media references, tokens, and raw OpenIDs from production logs.

Risk: Preview, upload, CloudBase, and message-push workflows can affect real mini program environments.

Mitigation: Review project configuration, appid, environment ID, and DevTools confirmation prompts before making write, deploy, upload, or publish changes.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local sibling CloudBase skills when installed; otherwise it asks the user to install the missing skill rather than fetching remote skill text.]

## Skill Version(s):

1.28.57 (source: server release metadata); artifact frontmatter reports 2.34.4

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
