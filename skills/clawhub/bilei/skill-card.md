## Description:

An evidence-led shopping advisor that checks product safety and reliability signals, audits manufacturers, and compares value before making a recommendation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhashushu](https://clawhub.ai/user/zhashushu)

### License/Terms of Use:

MIT

## Use Case:

External consumers can provide a product category, budget, and needs to compare available options. The skill gathers and grades safety, reliability, pricing, and manufacturer evidence, then explains its recommendation and data gaps.

### Deployment Geography for Use:

Global; its evidence sources and regulatory checks are China-focused.

## Known Risks and Mitigations:

Risk: The security review had partial component coverage, so its benign verdict does not cover every component fully.

Mitigation: Review the remaining component and complete a full security scan before deployment.

Risk: An unpinned installation can change between releases.

Mitigation: Install a specific reviewed release and inspect updates before upgrading.

Risk: Recommendations depend on current external pricing, recall, and testing information.

Mitigation: Check cited sources and dates, and reverify prices and safety records before purchase.

## Reference(s):

- [Source credibility and evidence grading](references/source-credibility.md)
- [Manufacturer and supply-chain audit](references/manufacturer-audit.md)
- [ClawHub release page](https://clawhub.ai/zhashushu/skills/bilei)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown report with evidence links and comparison tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conclusion-first recommendations with evidence grades, price trade-offs, manufacturer findings, and a five-tier ranking when supported by evidence.]

## Skill Version(s):

4.3.2 (source: frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
