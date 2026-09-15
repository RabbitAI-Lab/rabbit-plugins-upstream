## Description:

Operates the currencyapi connector through the OOMOL oo CLI to convert monetary amounts, retrieve latest or historical exchange rates, list supported currencies, and check account quota usage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to have an agent retrieve currency exchange data, convert monetary amounts, and check currencyapi account quota through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote OOMOL CLI installer scripts from cli.oomol.com.

Mitigation: Review the installer or use a pinned, verified CLI installation method before running setup commands, and avoid elevated shells unless required.

Risk: The skill depends on the OOMOL oo CLI and server-side credential handling for currencyapi requests.

Mitigation: Install only when the OOMOL CLI delivery path and connected-account credential flow are acceptable for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-currencyapi)
- [currencyapi homepage](https://currencyapi.com)
- [OOMOL oo CLI repository](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with oo CLI command examples and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed oo CLI, OOMOL sign-in, and a connected currencyapi account; setup commands are only relevant after authentication or connection failures.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
