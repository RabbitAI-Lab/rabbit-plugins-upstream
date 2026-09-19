## Description:

Open Exchange Rates (openexchangerates.org). Use this skill for ANY Open Exchange Rates request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve supported currencies, convert amounts, and query current or historical Open Exchange Rates data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructions include running remote installer scripts directly in a shell.

Mitigation: Prefer a trusted, versioned, verifiable oo CLI package, or download and inspect the installer before running it.

Risk: Normal use depends on an authenticated OOMOL account and a connected Open Exchange Rates API key.

Mitigation: Run setup or reconnect only after an authentication, missing-scope, expired-credential, app, or billing error.

## Reference(s):

- [Open Exchange Rates homepage](https://openexchangerates.org)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON data for exchange-rate queries and conversions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
