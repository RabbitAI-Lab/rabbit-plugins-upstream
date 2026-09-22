## Description:

Guides agents through building, debugging, previewing, publishing, and optimizing WeChat Mini Program projects, including CloudBase integration when explicitly used.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to create, modify, debug, preview, deploy, publish, and promote WeChat Mini Program projects. It helps route Mini Program work across project structure, WeChat Developer Tools, miniprogram-ci, CloudBase, message push, customer-service replies, and search optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live CLI, npx, MCP, and DevTools commands may install packages, authenticate services, or act on cloud resources.

Mitigation: Review commands before execution, prefer pinned trusted package versions, and approve writes only for recognized projects and environments.

Risk: Preview, upload, cloud-function deployment, and message-push workflows can change Mini Program or CloudBase state.

Mitigation: Confirm appid, project path, environment ID, and deployment intent before running write operations or publishing experience builds.

Risk: Incorrectly mixing Web and Mini Program authentication patterns can weaken or break CloudBase integrations.

Mitigation: Use wx.cloud and Mini Program-specific identity guidance, and avoid Web SDK login flows unless the project scope explicitly changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [CloudBase environment creation](https://docs.cloudbase.net/quick-start/create-env)
- [WeChat Mini Program search optimization](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code, shell commands, configuration snippets, and file edits when used by an agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to inspect project configuration, run WeChat Developer Tools or miniprogram-ci commands, and prepare Mini Program or CloudBase code changes for user review.]

## Skill Version(s):

1.28.61 (source: server release metadata; artifact frontmatter reports 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
