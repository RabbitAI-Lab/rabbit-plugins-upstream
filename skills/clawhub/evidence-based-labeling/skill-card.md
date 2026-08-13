## Description:

构建、优化并应用证据化标签体系，支持开放式标签发现、半开放标引、闭集标引、标签定义、判定规则、试标、全量标引、人工复核队列，以及借助智慧芽/PatSnap MCP 进行证据增强。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and domain experts use this skill to design, refine, pilot, and run evidence-backed labeling systems over patents, scientific literature, product materials, technical intelligence, customer requirements, and other structured text. It separates business decisions, model judgments, external evidence, validation, and human review so labeling results remain traceable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source records or excerpts may be sent to PatSnap/Zhihuiya MCP services during evidence enrichment.

Mitigation: Confirm data-sharing approval before use, apply the skill's selective MCP policy, and record MCP provenance for external evidence calls.

Risk: Credentials could be mishandled if users paste API keys or token-bearing URLs into chat.

Mitigation: Configure API keys only through the MCP or client setup flow and do not store credentials, authorization headers, or raw credential-bearing URLs in outputs.

Risk: Ambiguous or weak evidence can produce incorrect formal labels or misleading coverage.

Mitigation: Use scope, freeze, and execution gates; keep candidate, formal, unclassified, and needs-review states separate; route unresolved cases to the review queue or taxonomy backlog.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/evidence-based-labeling)
- [Input and Output Contract](artifact/references/input-output-contract.md)
- [Workflow Modes](artifact/references/workflow-modes.md)
- [Quality and Review](artifact/references/quality-and-review.md)
- [Zhihuiya MCP Orchestration](artifact/references/zhihuiya-mcp-orchestration.md)
- [PatSnap/Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [PatSnap/Zhihuiya MCP Marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON/YAML configuration, CSV/XLSX workbook structures, validation reports, and shell commands for bundled helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include preserved source records, labeling results, evidence tables, taxonomy backlog, review queue, QA summary, task metadata, and MCP provenance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
