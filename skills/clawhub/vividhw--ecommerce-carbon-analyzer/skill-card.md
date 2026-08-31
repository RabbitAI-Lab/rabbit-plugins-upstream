## Description:

Ecommerce Carbon Analyzer helps an agent calculate total shipment weight, cost, and carbon emissions for e-commerce products, including BOM-based gift sets, by using MCP tools for product lookup, component details, and shipping calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vividhw](https://clawhub.ai/user/vividhw)

### License/Terms of Use:

MIT

## Use Case:

Developers and external users use this skill to answer logistics and sustainability questions such as calculating total weight, landed cost, and carbon emissions for e-commerce shipments. It is especially suited to products with BOM structures where packaging and component-level values must both be included.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional LLM-backed runs may send user questions and tool outputs to external model APIs.

Mitigation: Run offline_check.py for local validation when possible, and use LLM providers only in environments approved for the data being processed.

Risk: Verbose mode can print tool call arguments and results that may include sensitive operational details.

Mitigation: Avoid --verbose with sensitive data and review logs before sharing them.

Risk: Unpinned package ranges can resolve to newer dependency versions over time.

Mitigation: Pin or review dependency versions before production deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vividhw/skills/ecommerce-carbon-analyzer)
- [DeepSeek API](https://api.deepseek.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with calculation steps, expected numeric results, and optional shell commands for offline or LLM-backed MCP runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call local MCP tools and optional external LLM APIs when configured; offline_check.py supports local validation without API keys.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
