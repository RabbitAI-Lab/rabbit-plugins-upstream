## Description:

WebScraper.io (webscraper.io) helps an agent read, create, update, and delete WebScraper.io sitemaps and scraping jobs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate WebScraper.io Cloud from an agent, including inspecting action schemas, managing sitemaps and scraping jobs, downloading JSON Lines results, and retrieving connected account information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may execute mutable remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified, versioned, user-controlled process before using the skill.

Risk: Write and destructive WebScraper.io actions can change or delete sitemaps and scraping jobs.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Connector requests can fail or act unexpectedly if the account connection, scopes, or payload schema are stale.

Mitigation: Inspect the live action schema before building payloads and refresh the WebScraper.io connection only after an auth or scope error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-webscraper-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [WebScraper.io homepage](https://webscraper.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [WebScraper.io icon](https://static.oomol.com/logo/third-party/webscraper_io.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON payload guidance, and returned connector JSON descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; downloaded scraping results are JSON Lines when requested.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
