## Description:

WebScraper.io helps agents operate Web Scraper Cloud through the OOMOL `oo` CLI for reading, creating, updating, and deleting sitemaps and scraping jobs, and downloading scraping results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage WebScraper.io sitemaps and scraping jobs from an agent session, including listing resources, retrieving account or job data, creating or updating sitemaps, deleting targets, and downloading job results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes direct execution of a remote installer for the oo CLI.

Mitigation: Review the vendor installation guide first, prefer a pinned, signed, or checksum-verified installer, and require explicit user approval before running curl|bash or irm|iex commands.

Risk: Write and destructive actions can change or delete WebScraper.io sitemaps and scraping jobs.

Mitigation: Inspect the live action schema, review the exact payload, and confirm the target and expected effect with the user before running write or delete actions.

## Reference(s):

- [ClawHub WebScraper.io Skill Page](https://clawhub.ai/oomol/skills/oo-webscraper-io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [WebScraper.io Homepage](https://webscraper.io/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector responses are JSON and downloaded scraping results are JSON Lines.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect the live connector schema before constructing payloads; write and destructive actions require user confirmation of the exact target and effect.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
