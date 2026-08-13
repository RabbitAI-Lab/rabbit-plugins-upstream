## Description:

Spider Cloud helps agents use OOMOL's oo CLI to check credits, extract links, scrape public pages, and search the web through a connected Spider Cloud account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want an agent to run Spider Cloud account, link extraction, scraping, and search actions through an OOMOL-connected account instead of calling the Spider Cloud API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search and scrape actions may consume Spider Cloud credits or send public URLs to Spider Cloud.

Mitigation: Use the skill only for intended Spider Cloud tasks, check account credits when cost matters, and avoid submitting URLs the user does not want processed by the service.

Risk: First-time setup may install the oo CLI or connect a Spider Cloud account.

Mitigation: Run setup steps only after an auth, connection, or missing-command failure, and make the account-connection step explicit to the user.

Risk: Connector action inputs can change over time.

Mitigation: Inspect the live connector schema before building each action payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-spider)
- [Spider Cloud Homepage](https://spider.cloud)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON and may include execution metadata.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
