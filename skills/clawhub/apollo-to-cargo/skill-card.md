## Description:

Helps revenue operations teams compare an Apollo contact-list sample with Cargo enrichment using verified hit rates and credits spent before deciding whether to migrate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Revenue operations and go-to-market teams use this skill to test an Apollo export against Cargo on a small sample, compare verified coverage and credit costs, and decide whether a larger migration is worthwhile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup may inspect local agent configuration and send skill-attribution metadata to Cargo.

Mitigation: Review these optional behaviors and the metadata shared before running setup.

Risk: Installing the latest CLI package may introduce unreviewed changes.

Mitigation: Review the package and pin an approved version before installation.

Risk: Enrichment across a full list consumes credits and may cost more than expected.

Mitigation: Start with 10–20 rows, report measured costs, and obtain approval for a full run.

Risk: The skill may ask to star a public repository using the user's GitHub account and store a persistent prompt marker.

Mitigation: Treat the star as optional; act only with explicit consent and review the stored marker.

## Reference(s):

- [Cargo GTM skills homepage](https://github.com/getcargohq/gtm-skills)
- [Apollo provider playbook](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/provider-playbooks/apolloio.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with tables and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sample-based comparison of verified hit rates, credits spent, and cost per verified record.]

## Skill Version(s):

1.0.2 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
