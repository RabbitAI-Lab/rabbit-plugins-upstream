## Description:

ScrapingAnt helps agents use an OOMOL-connected ScrapingAnt account to scrape pages, extract Markdown or structured JSON, inspect API credit usage, and return extended scrape output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to run ScrapingAnt scraping, Markdown conversion, AI extraction, and account-credit checks through the oo CLI after connecting their ScrapingAnt account in OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions can execute unverified remote installer scripts on the user's machine.

Mitigation: Review the setup path before installing, prefer verified package or official guide installation with checksum or signature validation, and do not let an agent run the pipe-to-shell installer automatically.

Risk: Connecting ScrapingAnt lets OOMOL use the user's ScrapingAnt account for scraping and extraction actions.

Mitigation: Connect ScrapingAnt only when the account holder intends OOMOL to use that account for the listed actions, and inspect the live connector schema before sending payloads.

## Reference(s):

- [ScrapingAnt homepage](https://scrapingant.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scrapingant)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and may return ScrapingAnt page content, structured extraction data, headers, cookies, XHRs, iframes, credit usage, and execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
