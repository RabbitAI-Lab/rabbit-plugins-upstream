## Description:

Gov Procurement Analyst supports Chinese government procurement workflows with opportunity discovery, bid decision analysis, tender document drafting support, enterprise due diligence, compliance checks, policy comparison, and bid-collusion risk review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement teams, suppliers, bid agencies, and purchasing units use this skill to find public procurement opportunities, assess bid fit, prepare bid materials, review compliance risks, and maintain reusable procurement knowledge. Outputs are decision-support drafts and risk signals that require human review for legal, financial, and procurement decisions.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill stores procurement and enterprise-profile data locally, which may include sensitive business information.

Mitigation: Use it only in an approved local workspace, limit access to generated files and databases, and review any exported or shareable reports before distribution.

Risk: The skill uses network access to public procurement sites and may be affected by platform access rules, rate limits, login requirements, or anti-scraping controls.

Mitigation: Restrict use to public information, honor robots.txt and platform terms, keep conservative request pacing, and skip sources that require login, payment, CAPTCHA bypass, or non-public access.

Risk: Scheduled pushes, shareable reports, dependency installation, and hot-update behavior can move data or code outside the immediate analysis flow.

Mitigation: Confirm destinations, sources, and approval steps before enabling scheduled sharing, installing dependencies, or applying updates.

Risk: Generated bid, legal, compliance, pricing, and scoring guidance may be incomplete or misleading if source data is stale, limited, or inferred.

Mitigation: Treat outputs as drafts, check confidence labels, verify important facts against official sources, and require qualified human review before procurement or legal action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/gov-procurement-analyst)
- [README](README.md)
- [Procurement platforms and compliance guide](references/procurement-platforms.md)
- [Anti-scraping best practices](references/anti-scraping-best-practices.md)
- [Enterprise profiling and matching algorithms](references/enterprise-profiling.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON result files, shell command examples, and prose guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local procurement analysis files and reusable knowledge records; legal, bid, compliance, and scoring outputs are draft support requiring human review.]

## Skill Version(s):

4.9.0 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
