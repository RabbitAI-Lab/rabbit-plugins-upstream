## Description:

Runs the Crossref Works Search Scraper BrowserAct template to extract structured public data from Crossref works search results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and automation users use this skill to run a BrowserAct workflow that collects Crossref works search results for reporting, enrichment, monitoring, and downstream dataset analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow requires a BrowserAct API key and could expose credentials if the key is pasted into chat or stored casually.

Mitigation: Set BROWSERACT_API_KEY through a local environment variable or secret manager and avoid sharing the key in conversation.

Risk: The BrowserAct workflow can browse outside the stated Crossref scope.

Mitigation: Keep invocations limited to https://search.crossref.org/search/works and review requested base_url values before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/crossref-works-search-scraper-api-skill)
- [BrowserAct API key console](https://www.browseract.com/reception/integrations?co-from=crossref-works-search-scraper)
- [Crossref works search](https://search.crossref.org/search/works)
- [BrowserAct v3 bots API endpoint](https://api.browseract.com/v3/bots)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API response output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires BROWSERACT_API_KEY; the helper polls BrowserAct run status for up to 900 seconds and returns the run payload when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
