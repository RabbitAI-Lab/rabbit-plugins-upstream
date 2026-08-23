## Description:

Gov Procurement Analyst helps suppliers, procurement agents, and purchasing organizations analyze Chinese government procurement opportunities, bid decisions, supplier profiles, compliance risks, contracts, policies, and proposal materials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External suppliers, bid managers, procurement agents, and purchasing teams use this skill to find public procurement opportunities, evaluate whether to bid, prepare bid materials, check compliance risks, and summarize procurement policy or contract issues.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill may process local enterprise profiles, bid history, and procurement documents that contain sensitive commercial information.

Mitigation: Use it only in an approved WorkBuddy environment, avoid confidential or classified bid materials unless that environment is cleared for them, and review local storage and retention before use.

Risk: The skill performs public-site collection and broad automation across government procurement sources.

Mitigation: Keep collection limited to public information, respect robots.txt and rate limits, and disable scheduled or large-scale collection unless the organization has approved that use.

Risk: Optional scheduled pushes or connector integrations can expose procurement updates or analysis to unintended recipients.

Mitigation: Enable outbound push only with approved connectors, verified recipients, and a review process for generated content before distribution.

Risk: Dependency installation, connector setup, or hot-update prompts can change runtime behavior.

Mitigation: Review dependency changes, connector permissions, and update prompts before accepting them in a production workspace.

## Reference(s):

- [README](README.md)
- [Data Source Platform List and Compliance Guide](references/procurement-platforms.md)
- [Anti-Scraping and Data Collection Best Practices](references/anti-scraping-best-practices.md)
- [Enterprise Profiling and Matching Algorithm Reference](references/enterprise-profiling.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON files, shell commands, and generated document content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local analysis files, procurement reports, bid document drafts, compliance findings, and operational guidance.]

## Skill Version(s):

5.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
