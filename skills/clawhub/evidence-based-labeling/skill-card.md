## Description:

构建、优化并应用证据化标签体系，适用于专利、科研文献、产品资料、技术情报、客户需求和其他结构化文本。可用于开放式标签发现、半开放标引、闭集标引、标签定义、默认或自定义判定规则、试标、Excel/CSV 全量标引、人工复核队列，以及借助智慧芽/PatSnap MCP 进行术语、样本、专利、文献和证据增强。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and domain experts use this skill to build, validate, pilot, and run evidence-backed labeling workflows over patents, scientific literature, product materials, technical intelligence, customer requirements, and other structured text. It supports discovery, semi-open, and closed labeling modes with taxonomy governance, review queues, QA checks, and selective PatSnap/Zhihuiya MCP evidence enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can selectively use PatSnap/Zhihuiya MCP services for evidence enrichment, which may expose submitted records or dataset excerpts to external services.

Mitigation: Use the skill only with data approved for the configured MCP services, avoid sensitive datasets unless approved, and keep API keys in MCP or client configuration rather than chat.

Risk: Labeling outcomes can be incorrect or misleading if users skip taxonomy confirmation, evidence review, or output validation.

Mitigation: Use the scope, freeze, and execution gates; preserve formal, candidate, unclassified, and needs_review statuses; run the included validation helpers before relying on final outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/evidence-based-labeling)
- [Input and Output Contract](references/input-output-contract.md)
- [Workflow Modes](references/workflow-modes.md)
- [Default Decision Rules](references/default-decision-rules.md)
- [Taxonomy Design](references/taxonomy-design.md)
- [Quality and Review](references/quality-and-review.md)
- [Zhihuiya MCP Orchestration](references/zhihuiya-mcp-orchestration.md)
- [PatSnap/Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)
- [PatSnap/Zhihuiya MCP Server Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured CSV, YAML, JSON, and workbook outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate task configs, taxonomy files, decision rules, evidence tables, labeling results, review queues, QA summaries, and MCP provenance records.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
