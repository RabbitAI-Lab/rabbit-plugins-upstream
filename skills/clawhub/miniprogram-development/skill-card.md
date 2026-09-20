## Description:

Helps agents build, debug, preview, publish, optimize, and integrate CloudBase features in WeChat Mini Program projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill when working on WeChat Mini Program projects that need project-structure guidance, DevTools preview/upload workflows, CloudBase integration, message push or customer-service behavior, and WeChat search optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real WeChat Mini Program uploads, CloudBase deployments, and customer-service messaging.

Mitigation: Require explicit user confirmation before login, upload, deploy, cloud-write, message-push, or customer-service actions.

Risk: Fallback CloudBase MCP instructions use unpinned npm package resolution.

Mitigation: Pin and review npm package versions before running CloudBase MCP or mcporter commands.

Risk: Incorrect mini program guidance can mix Web SDK authentication or unsupported tool paths into WeChat projects.

Mitigation: Follow the skill's platform-specific references and verify project configuration, appid, environment ID, and available DevTools commands before making changes.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [CloudBase Create Environment](https://docs.cloudbase.net/quick-start/create-env)
- [WeChat Mini Program Search SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with code, configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose preview, upload, deploy, or cloud-operation commands that require user confirmation before execution.]

## Skill Version(s):

1.28.59 (source: server release evidence; artifact frontmatter version is 2.34.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
