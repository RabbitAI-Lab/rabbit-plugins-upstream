## Description: <br>
Pricing helps agents set, test, and change prices across value metrics, packaging, discounts, price increases, willingness-to-pay research, pricing pages, enterprise quotes, international markets, and marketplace take rates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external operators, founders, and pricing teams use this skill to produce pricing recommendations, change plans, research plans, experiment designs, discount policies, price pages, and local pricing memory for commercial products and services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may automatically write or delete shared local business records containing customer, deal, margin, rate, due-date, and pricing information. <br>
Mitigation: Review before installing if automatic local pricing memory is not desired, keep backups of the Clawic data directories, and avoid providing confidential records unless local persistence is acceptable. <br>
Risk: Pricing guidance can affect customer communications, discounts, renewals, and regulatory presentation requirements if applied without review. <br>
Mitigation: Keep a human in the loop for live billing changes and customer-facing messages, and verify jurisdiction-specific pricing, renewal, fee, and disclosure rules before shipping. <br>
Risk: Pasted contracts, billing exports, or admin screenshots may contain credentials or sensitive access details. <br>
Mitigation: Store only pointers to secrets and strip credential values before any local memory write. <br>


## Reference(s): <br>
- [ClawHub Pricing skill page](https://clawhub.ai/ivangdavila/skills/pricing) <br>
- [Pricing skill homepage](https://clawic.com/skills/pricing) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [The Value Metric](artifact/value-metric.md) <br>
- [Packaging](artifact/packaging.md) <br>
- [Willingness-to-Pay Research](artifact/research.md) <br>
- [Price Experiments](artifact/testing.md) <br>
- [Compliance](artifact/compliance.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and plain text guidance, often with pricing tables, formulas, policies, plans, and local memory-file content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May maintain local pricing, contact, and project records under declared Clawic data paths; it does not change live billing systems or send customer communications.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
