## Description:

Sorftime (sorftime.com). Use this skill for ANY Sorftime request - searching and reading data. Whenever a task involves Sorftime, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ecommerce operators use this skill to run Sorftime-powered Amazon and Walmart US product, keyword, category, ranking, review, sales, and account-usage lookups through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet-to-shell installer commands.

Mitigation: Review the setup path before installing, prefer official versioned installers or verified package-manager installs, and do not run installer commands from an elevated shell.

Risk: Sorftime connector actions can consume account request credits.

Mitigation: Confirm high-cost or repeated lookups with the user and monitor credit balance or request usage when needed.

## Reference(s):

- [Sorftime homepage](https://www.sorftime.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sorftime)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect Sorftime action schemas and run connector actions; many actions consume Sorftime request credits.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
