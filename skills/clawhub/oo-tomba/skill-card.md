## Description:

Tomba (tomba.io) helps agents search and read contact, company, email verification, enrichment, LinkedIn, technology, and account data through an OOMOL-connected Tomba account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Tomba through an OOMOL-connected account for domain search, email finding, email verification, enrichment, LinkedIn lookup, company search, technology detection, and account reads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer scripts for the oo CLI.

Mitigation: Review the installer source or use a verified package-manager installation path before installing the CLI.

Risk: The skill uses the user's connected OOMOL and Tomba account to search or read contact and company data.

Mitigation: Run actions only in the intended connected account and review the live action schema and payload before execution.

## Reference(s):

- [Tomba homepage](https://tomba.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-tomba)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI and may return JSON responses from the connected Tomba service.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
