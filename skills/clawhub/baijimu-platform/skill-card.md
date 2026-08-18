## Description:

通过 `baijimu` CLI 使用百积木企业 AI 操作系统，用于登录认证、管理工作区、项目文件和 Git、智能体会话、模型凭证、Bundle-first 模块开发与统一发布、运行时服务与应用、托管服务、数据库配置、平台应用、本地 Connector，并通过公开 Partner API 补充 CLI 尚未封装的能力。

This skill is ready for commercial/non-commercial use.

## Publisher:

[momoplan](https://clawhub.ai/user/momoplan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to guide agents that manage Baijimu platform resources through the local `baijimu` CLI. It helps agents discover CLI capabilities, verify authentication and resource state, perform Bundle-first development and release workflows, and handle sensitive operations with explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad Baijimu platform operations, including writes, releases, deletions, rollbacks, database releases, external messages, and Partner API calls.

Mitigation: Review commands before approving sensitive actions, confirm exact targets and parameters, and verify results with platform state after execution.

Risk: Baijimu credentials, tokens, model keys, cookies, or complete authentication responses could be exposed if an agent prints secret-bearing output.

Mitigation: Keep credentials and tokens out of chat output and avoid options that display secrets unless the user explicitly requests them.

Risk: Using stale or mismatched CLI documentation can cause incorrect commands or parameters.

Mitigation: Use the installed CLI capability output and fixed-version documentation links as the execution source of truth.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/momoplan/skills/baijimu-platform)
- [Publisher profile](https://clawhub.ai/user/momoplan)
- [Source homepage](https://github.com/momoplan/baijimu-platform-skill)
- [Baijimu documentation](https://docs.baijimu.com/)
- [Baijimu CLI documentation](https://docs.baijimu.com/cli/)
- [Bundle development guide](https://docs.baijimu.com/development/bundle-development/)
- [Bundle change and release checklist](https://docs.baijimu.com/development/bundle-development/change-and-release/)
- [HTTP methodBody source contract](https://docs.baijimu.com/development/bundle-development/module-development/http-method-body/)
- [Partner API documentation](https://docs.baijimu.com/integration/api/)
- [Project concepts](https://docs.baijimu.com/concepts/projects/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include stable resource IDs, verification evidence, and concise error classification after CLI operations.]

## Skill Version(s):

1.5.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
