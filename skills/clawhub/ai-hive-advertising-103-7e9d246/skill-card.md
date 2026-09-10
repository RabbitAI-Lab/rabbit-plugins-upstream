## Description:

Helps agents plan and execute an AI-HIVE workflow for premium scarf-pattern and equestrian graphic advertising assets, including rights checks, model routing, sample generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand marketers, ecommerce merchants, advertising agencies, retail teams, and content marketing teams use this skill to create AI-HIVE advertising plans and assets for premium scarf-pattern and equestrian graphic campaigns while tracking rights, budget, paid-action approvals, and acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles credentials for a paid third-party MCP service.

Mitigation: Prefer OAuth through a trusted MCP client and keep API keys only in secrets or environment variables.

Risk: Paid generation, uploads, batch runs, sending, or public publishing could occur without enough user review.

Mitigation: Confirm price, model, scope, and user approval before any generation, upload, batch, send, or publish action.

Risk: The MCP endpoint can be overridden through AI_HIVE_MCP_URL.

Mitigation: Avoid setting AI_HIVE_MCP_URL unless deliberately testing a trusted endpoint, and review the environment before use.

Risk: The skill has broader-than-necessary invocation paths.

Mitigation: Use only with explicit AI-HIVE advertising tasks and verify that the requested scope matches the skill before invoking external tools.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-103-7e9d246)
- [AI-HIVE Workbench](https://ai-hive.iclip.cn/chat)
- [原创实施卡](references/original-workflow.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP Configuration Example](references/mcp-config.example.json)
- [API Key MCP Configuration Example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON work orders, shell commands, and MCP configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit confirmation before paid generation, uploads, batch runs, sending, or public publishing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
