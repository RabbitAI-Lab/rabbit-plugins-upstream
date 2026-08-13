## Description:

Generates a professional HTML report that analyzes competitors' recent global patent activity by brand patent clusters, technology-route trends, and country-level coverage for executive patent landscape reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, patent teams, and client-facing strategy teams use this skill to turn industry, competitor brand, client, and report-style inputs into an executive patent landscape report focused on competitor product-strategy signals rather than infringement analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external patent data MCP service and requires user authorization.

Mitigation: Confirm the patent MCP service configuration and account authorization before relying on database-backed findings.

Risk: Client-specific strategy details and generated reports may be stored in session output.

Mitigation: Avoid entering unnecessarily sensitive client strategy information when session storage is shared or retained.

Risk: Patent search results are top-k samples and may not represent the full competitive landscape.

Mitigation: Treat rankings and strategy conclusions as sample-based, and review the report methodology before executive use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/competitive-patent-landscape)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Report template reference](references/REPORT_TEMPLATE.md)
- [Patent search strategy reference](references/SEARCH_STRATEGY.md)

## Skill Output:

**Output Type(s):** [text, code, configuration, guidance]

**Output Format:** [HTML report with charts, narrative analysis, and patent strategy recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a client-specific HTML report to the session output when the required patent data MCP service is configured; otherwise it can provide an analysis framework.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
