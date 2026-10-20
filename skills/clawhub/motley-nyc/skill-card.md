## Description:

Helps families compare New York City neighborhoods and schools and understand school admissions using Motley's hosted data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bitbrujo](https://clawhub.ai/user/bitbrujo)

### License/Terms of Use:

MIT-0

## Use Case:

Families and their advisers use this skill to research New York City neighborhoods, compare schools and resources, and understand admissions requirements and timelines.

### Deployment Geography for Use:

Global (information covers New York City)

## Known Risks and Mitigations:

Risk: The skill suggests automatically approving remote tools, but their read-only behavior is asserted rather than independently enforced here.

Mitigation: Review the remote service and retain normal tool-approval policies before connecting.

Risk: School admissions details and neighborhood scores may be mistaken for guaranteed outcomes or current information.

Mitigation: Do not estimate admission odds; surface score dates and check published application timelines when they matter.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bitbrujo/skills/motley-nyc)
- [Motley MCP homepage](https://motley.nyc/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links, dated scores, and admissions timelines; does not access saved research or simulate lotteries.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
