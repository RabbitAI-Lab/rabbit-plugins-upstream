## Description:

Navigate Amazon as buyer, seller, or affiliate with price tracking, listing optimization, and smart purchasing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

External users, sellers, affiliates, and developers use this skill to research Amazon products, evaluate prices and deals, manage selling workflows, and prepare compliant affiliate guidance with human confirmation for sensitive account or purchase actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Purchase or seller-account actions can affect payment, shipping, inventory, or account status.

Mitigation: Require explicit human approval before purchases or seller-account actions, show totals and destination details, and prefer official Amazon APIs or manual confirmation for account-sensitive workflows.

Risk: Amazon credentials, payment details, tax IDs, and bank information are sensitive and should not be exposed to the agent.

Mitigation: Do not provide passwords, payment details, tax IDs, or bank data; use user-entered authentication, scoped sessions, and approved secret storage where credentials are unavoidable.

Risk: Amazon policy, affiliate disclosure, scraping, and automation mistakes can create account or compliance risk.

Mitigation: Use official APIs when available, rate-limit public data access, avoid prohibited automation, and require clear affiliate disclosures before monetized links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/amazon)
- [Buying workflows](artifact/buying.md)
- [Price tracking and deal detection](artifact/pricing.md)
- [Seller operations](artifact/selling.md)
- [Amazon Associates](artifact/affiliates.md)
- [Security protocols](artifact/security.md)
- [Legal and compliance](artifact/legal.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text recommendations, checklists, comparisons, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product comparison tables, price-alert criteria, affiliate-link guidance, and human-confirmation steps for purchases or account-sensitive actions.]

## Skill Version(s):

1.0.1 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
