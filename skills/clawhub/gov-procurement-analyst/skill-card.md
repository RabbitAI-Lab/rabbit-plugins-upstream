## Description:

Gov Procurement Analyst helps suppliers, procurement agents, and purchasing units analyze Chinese public procurement opportunities, bid fit, bid documents, supplier background, compliance issues, competitor strategy, and post-bid follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement teams, suppliers, and purchasing organizations use this skill to discover public procurement opportunities, assess whether to bid, draft or review bid materials, profile competitors, and track compliance-sensitive follow-up tasks.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill can store sensitive business, bidding, project history, and company identifier data for later analysis.

Mitigation: Use only necessary data, avoid entering confidential or non-public procurement material, and periodically delete local databases when long-term reuse is not needed.

Risk: Webhook alert integrations can send procurement or company context to external collaboration systems.

Mitigation: Configure only required push integrations and review webhook recipients, payload content, and access controls before enabling alerts.

Risk: Broad triggers and inconsistent privacy wording may make data handling expectations unclear for real bid workflows.

Mitigation: Review the security guidance before installation and limit inputs to public, procurement-safe information unless the organization has approved the workflow.

## Reference(s):

- [Data Source Platform List and Compliance Guide](references/procurement-platforms.md)
- [Anti-Scraping Strategy and Data Collection Best Practices](references/anti-scraping-best-practices.md)
- [Enterprise Profiling and Matching Algorithm Reference](references/enterprise-profiling.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, structured tables, bid templates, JSON-like analysis data, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include procurement scores, confidence notes, local file paths, and webhook or dependency configuration guidance.]

## Skill Version(s):

5.3.0 (source: frontmatter, release evidence, README version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
