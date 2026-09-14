## Description:

Helps Chinese-speaking Fotor and Fotor懒设计 users run same-input migration trials against AI-HIVE models before deciding which generative visual-design steps to move.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and small businesses use this skill to compare their existing Fotor/Fotor懒设计 visual-design tasks with AI-HIVE using authorized samples, current model availability, pricing, and clear rollback criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE credentials could be sent to an unexpected custom MCP endpoint if the endpoint override is changed.

Mitigation: Use OAuth or a tightly scoped AI-HIVE API key, avoid overriding AI_HIVE_MCP_URL unless the endpoint is trusted, and revoke any key used with an unexpected endpoint.

Risk: Model generation, uploads, batch runs, publishing, or stopping an existing service can create cost, privacy, or business-impact risk.

Mitigation: Require explicit user confirmation before paid, batch, upload, publishing, or service-discontinuation actions.

Risk: Comparisons involving Fotor/Fotor懒设计 can mislead users if they imply affiliation, full replacement, or use unlicensed brand assets.

Mitigation: State that third-party marks belong to their owners, use only authorized input materials, and compare outputs with the same inputs and acceptance criteria.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-cn-name-fotor-lansheji)
- [AI-HIVE Workbench](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP Endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Fotor懒设计 Chinese Name Evidence](https://www.fotor.com.cn/company/services)
- [Chinese Name Evidence](artifact/references/chinese-name-evidence.md)
- [MCP Binding Guide](artifact/references/mcp-binding.md)
- [Migration Workflow](artifact/references/migration-workflow.md)
- [Source and Boundary](artifact/references/source-and-boundary.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and optional local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a local migration-plan.json when the included planning script is run.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
