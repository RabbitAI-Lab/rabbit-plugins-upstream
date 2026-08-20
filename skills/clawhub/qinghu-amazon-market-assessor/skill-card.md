## Description:

青虎AI 亚马逊细分市场评估 helps an agent assess category entry viability from market size, sales, listing and brand concentration, price-band opportunity, seller geography, new-product activity, demand trends, and return-rate signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, ecommerce operators, and market researchers use this skill to decide whether to enter a product category and to identify viable price bands, competitive risks, and market-entry conditions before investing in inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Qinghu API token and may read it from user-provided input or supported environment variables.

Mitigation: Install only where Qinghu credential handling is acceptable, keep tokens scoped and rotated, and avoid exposing token values in shared transcripts or exported files.

Risk: Some Qinghu tool calls may be paid, and the skill can approve multiple market-analysis calls after user authorization.

Mitigation: Review paid-call authorization prompts, confirm the intended tools before proceeding, and track reported Qinghu point consumption after calls complete.

Risk: Large market datasets may be exported to local spreadsheet files by default.

Mitigation: Run the skill in a workspace where local exports are expected, review generated files before sharing, and remove sensitive exports when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-amazon-market-assessor)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with concise recommendations, supporting metrics, JSON examples, shell command examples, and spreadsheet exports when large datasets are returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs emphasize an entry recommendation, market profile, competition structure, price-band guidance, and risk list; datasets of ten or more records are expected to be exported to local spreadsheet files when available.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
