## Description:

Use this skill to search and look up records in the iTunes Store and Apple Books Store through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search iTunes Store and Apple Books Store content or look up store records by identifier without calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup uses remote installer commands that can execute network-fetched code on the user's machine.

Mitigation: Run installer commands only after confirming trust in OOMOL's installer distribution, and prefer a signed or checksum-verified installation method when available.

Risk: Authentication and billing setup can affect the user's OOMOL account state or stop execution when credits are insufficient.

Mitigation: Attempt normal read-only actions first, perform sign-in only after an authentication failure, and stop for user action if the connector reports insufficient credit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-itunes-search)
- [iTunes Search API homepage](https://performance-partners.apple.com/search-api)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only iTunes search and lookup actions return connector responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
