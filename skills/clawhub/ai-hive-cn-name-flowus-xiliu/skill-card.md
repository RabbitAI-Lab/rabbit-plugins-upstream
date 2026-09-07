## Description:

This skill helps FlowUs users run a same-input AI-HIVE trial for document analysis workflows and decide which generative AI steps can migrate while preserving unsupported or proprietary functions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, individual operators, and small businesses use this skill to compare FlowUs document-analysis tasks with AI-HIVE on the same authorized samples, acceptance criteria, and budget constraints. The skill supports planning, MCP connection setup, model/tool discovery, and migration decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad remote AI-HIVE tool-calling can expose credentials or submitted data if credentials, prompts, or documents are handled carelessly.

Mitigation: Prefer OAuth through the MCP client, keep API keys in a secret store, do not paste tokens into chat or logs, and use only authorized test documents.

Risk: The AI_HIVE_MCP_URL override can direct requests to an untrusted endpoint.

Mitigation: Use the documented AI-HIVE MCP endpoint unless the alternate endpoint is fully trusted and reviewed.

Risk: Some AI-HIVE tool calls may create paid generation tasks or duplicate work after a timeout.

Mitigation: List tools and models first, require explicit confirmation for paid actions, record task IDs, and query existing tasks before retrying.

Risk: Migration conclusions can be misleading without same-input evidence or if the skill is read as an official FlowUs relationship.

Mitigation: Compare only authorized samples with the same acceptance criteria, keep FlowUs fallback paths, and preserve the stated no-affiliation and trademark boundaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-cn-name-flowus-xiliu)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [FlowUs product name evidence](https://flowus.cn/product)
- [FlowUs息流：中文名来源与去重](references/chinese-name-evidence.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [FlowUs息流迁移工作流](references/migration-workflow.md)
- [来源与品牌边界](references/source-and-boundary.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON work-plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires separate user confirmation before paid calls, batch generation, external sending, public publishing, or stopping an existing service.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
