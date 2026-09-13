## Description:

This skill helps users run the Crates.io Package Search Scraper BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and data practitioners use this skill to collect structured public crates.io search results for market research, dataset enrichment, monitoring, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a BrowserAct API key and may prompt users to provide it directly.

Mitigation: Set BROWSERACT_API_KEY through a local environment variable or secrets manager and do not paste the API key into chat or agent prompts.

Risk: The security verdict is suspicious and recommends review before installation.

Mitigation: Review the skill before installing and use it only for the intended crates.io BrowserAct scraping workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/cratesio-package-search-scraper-api-skill)
- [Crates.io](https://crates.io)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=cratesio-package-search-scraper)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; reports task status while waiting for BrowserAct results.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
