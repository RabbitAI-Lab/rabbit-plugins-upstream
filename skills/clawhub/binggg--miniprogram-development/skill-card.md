## Description:

WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects, including project structure, WeChat Developer Tools workflows, CloudBase integration, message push, customer-service auto-reply, and Mini Program search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, modify, debug, preview, deploy, publish, and optimize WeChat Mini Programs. It is especially useful when projects involve WeChat Developer Tools, wxide or miniprogram-ci workflows, CloudBase, message push, customer-service auto-replies, or WeChat search indexing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudBase fallback guidance can lead agents to run unpinned package commands for MCP tooling.

Mitigation: Pin package versions where possible, review packages before execution, avoid automatic -y installs for security-sensitive tooling, and use least-privilege cloud credentials.

Risk: Generated CloudBase examples can retain user-linked identifiers or message logs without enough privacy review.

Mitigation: Adjust tracing and logging to match the app privacy policy, log only necessary fields, and avoid retaining sensitive message content unless required.

Risk: Message-push or customer-service workflows may fail or encourage unsupported workarounds if agents bypass the documented IDE and wxide paths.

Mitigation: Use WeChat Developer Tools or wxide CLI for supported operations, do not teach low-level bypasses, and verify customer-service replies through the required OpenAPI permission and IDE logs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program Search Optimization](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [WeChat Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, command examples, checklists, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bilingual English and Chinese terminology for WeChat Mini Program and CloudBase workflows.]

## Skill Version(s):

1.28.49 (source: server release evidence; artifact frontmatter reports 2.33.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
