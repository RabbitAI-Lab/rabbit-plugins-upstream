## Description:

ScrapingAnt lets an agent use an OOMOL-connected ScrapingAnt account to scrape pages, convert pages to Markdown, extract structured data with AI, and check API credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to route ScrapingAnt tasks through OOMOL, including web scraping, Markdown conversion, AI-assisted data extraction, and subscription credit checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that can execute changing code on the user's machine.

Mitigation: Use a verified or manually reviewed oo CLI installation path before running ScrapingAnt connector actions.

Risk: Scraping actions depend on live connector schemas and account state.

Mitigation: Inspect the action schema before constructing payloads and use setup steps only after authentication, connection, or billing errors.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-scrapingant)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [ScrapingAnt Homepage](https://scrapingant.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return Markdown, structured JSON fields, extended scrape data, account status, and API credit information.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
