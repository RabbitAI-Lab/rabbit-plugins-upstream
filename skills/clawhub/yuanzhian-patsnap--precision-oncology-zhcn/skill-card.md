## Description:

This skill helps agents produce Chinese-language precision oncology reports by combining literature, epidemiology, clinical guidance, trial results, molecular biology, and commercial research signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Life science, oncology, pharmaceutical research, and business development users can use this skill to guide Chinese-language research on cancers, cancer mechanisms, standards of care, clinical trials, unmet needs, and market dynamics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on PatSnap's life-science MCP service and requires a PatSnap API key for normal operation.

Mitigation: Install it only when the user intends to use PatSnap MCP data, and configure the API key through the documented PatSnap MCP setup flow.

Risk: Loading the skill can make a small connectivity query to PatSnap before answering.

Mitigation: Review this behavior before deployment in environments where outbound service calls or credential use require approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/precision-oncology-zhcn)
- [PatSnap Life Sciences](https://eureka.patsnap.com/ls-landing)
- [PatSnap Developer Documentation](https://open.patsnap.com/devportal)
- [PatSnap Pharma Intelligence MCP Server](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [PatSnap Chemical Molecular MCP Server](https://open.patsnap.com/marketplace/mcp-servers/713886)
- [PatSnap Biology Modality MCP Server](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown reports with structured Chinese sections and inline shell commands for setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use uppercase Roman numeral chapters, lowercase Roman sub-sections, and a required conclusion section.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter metadata lists 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
