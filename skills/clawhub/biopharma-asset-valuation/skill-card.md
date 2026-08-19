## Description:

Combines rNPV, peak-sales, and comparable-deal methods to help biopharma BD teams value pipeline assets for licensing, out-licensing, and negotiation planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External BD, licensing, and business development teams use this skill to assemble transparent valuation assumptions, compare relevant biopharma deals, and generate a professional valuation report for negotiation preparation. It is decision-support material and should not be treated as a final investment recommendation or deal price.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated HTML reports load third-party CDN JavaScript.

Mitigation: Disable HTML output for sensitive reports or review the generated HTML before opening or sharing it.

Risk: Valuation formulas and disclosures may not align fully with the generated report narrative.

Mitigation: Review valuation assumptions, formulas, and report disclosures before using the output in deal discussions.

Risk: Asset assumptions may be shared with the configured pharma MCP during the workflow.

Mitigation: Use only data approved for that MCP environment and avoid entering confidential asset details unless sharing is permitted.

Risk: The valuation output can be mistaken for final deal-pricing or investment advice.

Mitigation: Treat the report as decision support and require expert BD, finance, legal, and scientific review before making business decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/biopharma-asset-valuation)
- [Full comparable BD transaction dataset](artifact/references/real_deals_1394.json)
- [Selected comparable BD transaction dataset](artifact/references/real_deals.json)
- [Optional HTML report chart library](https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus generated Markdown report files, with optional HTML and PPTX report outputs from the local Python runner.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON valuation inputs, local comparable-deal data, and the pharma_intelligence MCP as configured evidence sources.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
