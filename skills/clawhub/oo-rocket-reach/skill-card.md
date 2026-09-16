## Description:

RocketReach helps agents search and read RocketReach people, company, and account data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to look up RocketReach people, companies, funding, industry, company size, account profile, or lookup status data through an OOMOL-connected RocketReach account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes an unverified internet installer script for the oo CLI.

Mitigation: Prefer an official package-manager or verified release path; if using the documented installer, inspect it first and avoid elevated privileges.

Risk: Lookup and search actions use the user's OOMOL-connected RocketReach account and may consume applicable service credits.

Mitigation: Confirm the connected account and expected billing impact before running high-volume searches or repeated lookups.

## Reference(s):

- [RocketReach on ClawHub](https://clawhub.ai/oomol/skills/oo-rocket-reach)
- [RocketReach homepage](https://rocketreach.co)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas and returns data from the authenticated OOMOL-connected RocketReach account.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
