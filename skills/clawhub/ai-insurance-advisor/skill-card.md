## Description:

AI Insurance Advisor helps mainland China users analyze insurance needs, compare insurance products, estimate premiums, design coverage plans, answer insurance questions, and draft insurance sales support content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Consumers, families, and insurance sales professionals in mainland China use this skill to assess coverage gaps, compare static product data, estimate premiums, design insurance plans, answer insurance questions, and draft sales or training copy.

### Deployment Geography for Use:

China (mainland)

## Known Risks and Mitigations:

Risk: The skill may ask users for personal, family, health, income, mortgage, and budget details.

Mitigation: Collect only information needed for the insurance task, avoid unnecessary sensitive details, and handle user data according to applicable privacy and compliance obligations.

Risk: Insurance product data is static and includes quality caveats, so terms, availability, premiums, or licensing may be outdated.

Mitigation: Verify current product terms, premiums, eligibility, and sales channels with official insurers or qualified professionals before making financial decisions.

Risk: Generated insurance suggestions, compliance notes, and sales copy may be incomplete or unsuitable for a user's specific circumstances.

Mitigation: Treat outputs as advisory drafts and review them with qualified insurance, legal, or compliance professionals before relying on them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)
- [Publisher Profile](https://clawhub.ai/user/mnetfairy)
- [Insurance Knowledge Base](artifact/references/insurance-knowledge.md)
- [Compliance Reference](artifact/references/compliance.md)
- [Product Dataset](artifact/references/products.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Chinese Markdown responses plus JSON emitted by local Python helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses static local product data; product availability, terms, premiums, licensing, and sales recommendations require external verification.]

## Skill Version(s):

2.0.45 (source: server release metadata; artifact frontmatter says 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
