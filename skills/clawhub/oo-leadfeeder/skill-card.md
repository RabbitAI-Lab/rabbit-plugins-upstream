## Description:

Leadfeeder (leadfeeder.com). Use this skill for ANY Leadfeeder request - searching and reading data. Whenever a task involves Leadfeeder, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users use this skill to search and read Leadfeeder company intelligence through an OOMOL-connected account. It supports account, user, company, company matching, company search, and IP enrichment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute an unverified remote installer on the user's machine.

Mitigation: Review setup instructions before installation, prefer a verified and versioned oo CLI source with checksum or signature validation, and do not let an agent run the remote installer automatically.

Risk: Leadfeeder queries send requested company, account, user, or IP enrichment data through OOMOL's connector and Leadfeeder.

Mitigation: Only run queries for data the user intends to share with the connected services and inspect the connector schema before sending payloads.

## Reference(s):

- [Leadfeeder homepage](https://www.leadfeeder.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Leadfeeder connection](https://console.oomol.com/app-connections?provider=leadfeeder)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector schema inspection commands and JSON results from Leadfeeder actions.]

## Skill Version(s):

1.0.3 (source: server release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
