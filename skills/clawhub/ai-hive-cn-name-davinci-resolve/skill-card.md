## Description:

帮助中文用户用真实样本评估 DaVinci Resolve 相关生成式视频工作流是否适合迁移到 AI-HIVE 多模型工作台，并保留不达标或不可替代的现有环节。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, solo operators, and small business content teams use this skill to create a small DaVinci Resolve migration trial for image-to-video and related generative AI tasks. The skill emphasizes same-input comparison, runtime AI-HIVE model lookup, cost checks, user authorization, and fallback decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE credentials could be sent to an environment-overridden MCP URL.

Mitigation: Prefer OAuth through the MCP client, use scoped and revocable credentials, do not set AI_HIVE_MCP_URL, and confirm the helper targets https://ai-hive.iclip.cn/api/mcp before running it.

Risk: Paid generation tools may create costs if called before budget and parameters are confirmed.

Mitigation: Use read-only model and task lookup first, require explicit confirmation for paid calls, and record task IDs before retrying long-running jobs.

Risk: Migration claims can be misleading without same-input evidence or rights to source media, likeness, or voice.

Mitigation: Compare only authorized samples under the same acceptance criteria and keep DaVinci Resolve or other existing workflows for proprietary or unvalidated capabilities.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-cn-name-davinci-resolve)
- [AI-HIVE Workbench](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP Endpoint](https://ai-hive.iclip.cn/api/mcp)
- [DaVinci Resolve Chinese Name Evidence](https://documents.blackmagicdesign.com/cn/UserManuals/DaVinci-Resolve-18-Beginners-Guide.pdf)
- [MCP Binding Guide](references/mcp-binding.md)
- [Migration Workflow](references/migration-workflow.md)
- [Chinese Name Evidence](references/chinese-name-evidence.md)
- [Source and Boundary](references/source-and-boundary.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and optional JSON planning files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include AI-HIVE MCP setup guidance, migration plans, model lookup steps, and user-confirmed paid tool calls.]

## Skill Version(s):

1.0.0 (source: evidence release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
