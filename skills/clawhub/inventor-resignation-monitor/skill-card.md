## Description:

Generates HTML monitoring briefings that identify likely former inventors, review their recent patent activity at other organizations, compare technical similarity with the original company, and summarize risk levels and recommended actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise IP, legal, and competitive-intelligence teams use this skill to monitor whether inventors who may have left a target company are filing related patents elsewhere. The skill can work from a target company plus technical domain or from a named inventor list, then produces a structured risk briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain sensitive competitive intelligence.

Mitigation: Store and share generated reports only in approved workspaces for the relevant IP or legal team.

Risk: The HTML renderer embeds report fields directly, so untrusted or unreviewed JSON can introduce unsafe report content.

Mitigation: Use trusted data sources, review report JSON before rendering, and sanitize externally supplied text before HTML generation.

Risk: Patent publication delays and same-name inventors can make risk findings incomplete or imprecise.

Mitigation: Treat the briefing as triage, verify matches with patent metadata and technical experts, and rerun monitoring on a regular cadence.

Risk: Live patent retrieval depends on the configured PatSnap MCP integration and account authorization.

Mitigation: Confirm the PatSnap MCP service is intentionally enabled and authorized before relying on live search results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/inventor-resignation-monitor)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Inventor resignation monitoring workflow](references/workflow.md)
- [Inventor monitor data schema](references/data_schema.json)

## Skill Output:

**Output Type(s):** [Analysis, Files, Text, shell commands, Configuration instructions]

**Output Format:** [HTML report with terminal summary and optional generated analysis prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include inventor-level risk labels, patent comparison tables, and suggested follow-up actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
