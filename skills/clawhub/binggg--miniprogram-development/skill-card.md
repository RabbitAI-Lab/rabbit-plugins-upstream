## Description:

Helps agents build, debug, preview, publish, optimize, and integrate WeChat Mini Program projects, including project configuration, DevTools workflows, message and customer-service flows, search indexing, and CloudBase when explicitly used.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modify, debug, preview, deploy, publish, and promote WeChat Mini Programs. It is most useful when an agent needs platform-specific guidance for project structure, WeChat Developer Tools, miniprogram-ci, CloudBase integration, message push, customer-service auto-reply, or WeChat search optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents through live WeChat, CloudBase, deployment, message-push, and customer-service operations.

Mitigation: Use a test environment first, require explicit user confirmation before sends, uploads, routing changes, or deployments, and verify appid, project path, and CloudBase environment before execution.

Risk: Mutable tooling such as latest CLI packages or Nightly DevTools workflows can change behavior across sessions.

Mitigation: Pin reviewed tool versions where possible, inspect command help or tool schemas before use, and avoid inventing unavailable wxide or CloudBase MCP commands.

Risk: Message handling and logs may expose sensitive identifiers or conversation data such as openid values or full event payloads.

Mitigation: Avoid broad CloudBase credentials, redact sensitive identifiers in logs and shared output, and remove verbose event logging before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](artifact/references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](artifact/references/seo-search-optimization.md)
- [WeChat IDE Skills vs CloudBase MCP](artifact/references/wxide-vs-cloudbase-mcp.md)
- [Common Pitfalls](artifact/references/pitfalls.md)
- [WeChat DevTools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program Search SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include WeChat Mini Program file edits, project configuration guidance, CLI command proposals, and deployment or debugging checklists.]

## Skill Version(s):

1.28.48 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
