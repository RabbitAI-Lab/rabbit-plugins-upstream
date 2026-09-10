## Description:

This skill runs the Deep Website Scraper Bot BrowserAct template to extract structured public data from dynamic webpages for downstream analysis, reporting, enrichment, and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation teams use this skill to run a BrowserAct workflow that collects structured data from public webpages for market research, dataset enrichment, reports, trend discovery, and repeatable API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Target URLs and scraped results are processed by BrowserAct.

Mitigation: Use the skill only with public, non-sensitive URLs and avoid internal, private, signed, credential-bearing, or regulated pages.

Risk: The skill requires a BrowserAct API key.

Mitigation: Configure BROWSERACT_API_KEY locally and do not paste the key into chat or store it in the skill artifact.

Risk: Scraped output may include contact fields or other personal data.

Mitigation: Minimize collection and handle returned data according to applicable privacy, retention, and access-control requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/deep-website-scraper-agent-built-api-skill)
- [BrowserAct bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Terminal status text followed by the BrowserAct run response as JSON when execution succeeds.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a target website_url and a locally configured BROWSERACT_API_KEY; returned fields may include page metadata, content, contact fields, ratings, and source URLs when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
