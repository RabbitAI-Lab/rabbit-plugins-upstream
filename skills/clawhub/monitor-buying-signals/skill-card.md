## Description:

Monitors target accounts for recent public hiring, statements, and detection-feed events that may indicate buying intent, with dates and source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales development and account executive teams use this skill to monitor a target-account list for recent hiring, public statements, and detection-feed activity, then review dated source links to spot potentially relevant timing. It supports research about when a conversation may be relevant; it does not establish a basis for outreach or score account fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The account watchlist is shared with Cargo and connected integrations during monitoring.

Mitigation: Use only a watchlist you are comfortable sharing with those services.

Risk: Paid lookups and recurring runs can incur credits as returned jobs and accounts accumulate.

Mitigation: Start with a 10–20 account sample, report the observed cost and credit estimate, and get approval before a full run.

Risk: A public signal could be mistaken for permission to contact someone.

Mitigation: Treat signals as research unless an independent, documented basis for outreach exists; public activity alone is not a basis.

## Reference(s):

- [Cargo GTM skills repository](https://github.com/getcargohq/gtm-skills)
- [Tech intent recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/tech-intent.md)
- [Account expansion recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/account-expansion.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown tables with dated signal descriptions and source links, plus inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports accounts with detected signals; separates timing research from fit scoring and outreach decisions.]

## Skill Version(s):

1.0.4 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
