## Description:

StoreCensus helps agents search and read ecommerce intelligence, Shopify app data, and ecommerce store records through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve StoreCensus ecommerce intelligence for website domains or lead IDs, list and search Shopify apps, and search ecommerce stores through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes direct execution of remote installer scripts for the oo CLI.

Mitigation: Review the installer source before use, prefer a trusted package manager or manually downloaded installer, and do not let an agent run the remote installer automatically.

## Reference(s):

- [StoreCensus ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-storecensus)
- [StoreCensus Homepage](https://www.storecensus.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include StoreCensus connector responses returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
