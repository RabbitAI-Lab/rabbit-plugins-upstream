## Description:

Research Amazon products, track prices, and compare deals. Use when searching for products on Amazon, monitoring price changes, creating wishlists with price alerts, or comparing product specifications and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jcbuer](https://clawhub.ai/user/jcbuer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Amazon products, manage a local price-tracking database, compare products, maintain wishlists, and create target-price alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic price checks and alerts may show simulated or misleading prices rather than verified Amazon prices.

Mitigation: Treat generated price history and alerts as unverified; manually confirm prices on Amazon before purchasing or sharing recommendations.

Risk: The bundled cron setup installs persistent daily execution for the current account.

Mitigation: Review the cron entry before installation, do not run setup as root, and use targeted crontab editing instead of broad removal commands.

Risk: The skill stores product, wishlist, alert, and price history data in a local SQLite database.

Mitigation: Use it only where local shopping data storage is acceptable and protect or delete the database according to the user's privacy requirements.

## Reference(s):

- [Amazon Recherche - Alu-Profile 20x20](references/alu_profile_guide.md)
- [ClawHub Skill Page](https://clawhub.ai/jcbuer/skills/amazon-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local SQLite records, logs, and cron configuration when users run the bundled scripts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
