## Description:

Scrape Creators lets an agent discover endpoints, check credit balance, and invoke documented Scrape Creators API endpoints through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent search and read Scrape Creators data, inspect endpoint schemas, check credit balance, and invoke documented endpoints through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can use the user's OOMOL-connected Scrape Creators account.

Mitigation: Install this skill only when account-backed Scrape Creators access is intended.

Risk: API calls may consume Scrape Creators or OOMOL credits.

Mitigation: Review payloads for expensive or ambiguous requests before execution.

Risk: First-time setup may require installing the oo CLI or connecting an account.

Mitigation: Run setup only from trusted OOMOL sources and only after an auth or connection failure requires it.

## Reference(s):

- [Scrape Creators homepage](https://scrapecreators.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Scrape Creators connection](https://console.oomol.com/app-connections?provider=scrape_creators)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command responses include data and meta.executionId when actions run.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
