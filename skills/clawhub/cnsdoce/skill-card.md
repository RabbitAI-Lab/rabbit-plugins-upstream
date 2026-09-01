## Description:

Cnsdoce Publish V5 helps agents query Chinese construction-cost quota items, calculate Shandong/Jinan engineering fees, check unit and price assumptions, and prepare quotation-table outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoshun-sudo](https://clawhub.ai/user/caoshun-sudo)

### License/Terms of Use:

MIT

## Use Case:

External users and cost engineers use this skill to map Chinese engineering bill items to quota items, calculate construction fees, validate unit conversions and material prices, and prepare quotation table outputs for Shandong/Jinan-focused projects.

### Deployment Geography for Use:

China, with Shandong and Jinan costing sources emphasized

## Known Risks and Mitigations:

Risk: Project descriptions, pricing details, or API credentials may be processed by third-party LLM providers when LLM features are configured.

Mitigation: Use API keys only intentionally, disclose data handling to users before LLM use, and prefer --no-llm or local-only workflows for confidential bids.

Risk: A configurable LLM endpoint could route project data to an untrusted host.

Mitigation: Do not set HUNYUAN_URL to an untrusted host; verify endpoint configuration before running LLM-assisted matching.

Risk: Database migration can change quota.db content used for costing decisions.

Mitigation: Back up quota.db before running migration scripts and review migrated data before relying on it for pricing.

Risk: Built-in sample quota data may be insufficient for formal pricing decisions.

Mitigation: Use authorized source data for formal projects and require human review of quota matches, unit conversions, and quotation outputs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/caoshun-sudo/skills/cnsdoce)
- [Cost composition reference](references/cost_composition.md)
- [Fee standard reference](references/fee_standard.md)
- [Unit conversion reference](references/unit_conversion.md)
- [Multi-quota mapping reference](references/multi_quota_mapping.md)
- [Measure item reference](references/measure_items.md)
- [Other item reference](references/other_items.md)
- [Tencent TokenHub chat completions endpoint](https://tokenhub.tencentmaas.com/v1/chat/completions)
- [Volces Doubao chat completions endpoint](https://ark.cn-beijing.volces.com/api/v3/chat/completions)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON snippets, shell commands, and quotation-table or Excel output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use optional third-party LLM APIs when configured; local no-LLM workflows are available for confidential work.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter: 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
