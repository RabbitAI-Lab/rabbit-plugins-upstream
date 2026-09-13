## Description:

This skill helps agents research Douyin blue-ocean product opportunities by combining Qinghu Douyin trend and video data with 1688 product sourcing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product researchers, and commerce operators use this skill to identify niche Douyin demand, validate content heat and supply gaps, and connect promising products to 1688 sourcing options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a Qinghu API token that may be exposed to the runtime.

Mitigation: Provide the token only in trusted environments, prefer environment variables over chat text when available, and avoid logging or exporting the token.

Risk: Some Qinghu API calls may consume paid credits.

Mitigation: Request user approval before tool calls, rely on returned pointCost values for reporting, and stop when authorization is missing or unclear.

Risk: Larger research results may be exported to local files by default.

Mitigation: Review generated files before sharing them and avoid storing sensitive business notes in exported datasets.

Risk: Douyin trend signals can be mistaken for purchase demand.

Mitigation: Cross-check trends with keyword video data, hashtag details, 1688 supply data, pricing, and margin assumptions before ranking products.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-douyin-bluesea-collector)
- [AutoAGC publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu API endpoint](https://www.iqinghu.com/api/desktop/qh/mcp)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON examples, API-call instructions, and optional exported table files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export larger result sets to local table files and should report Qinghu pointCost-derived usage when paid calls are made.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
