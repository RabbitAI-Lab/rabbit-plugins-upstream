## Description:

Runs the Google Trends Interest Scraper BrowserAct template to collect public Google Trends Explore data and return structured results for analysis or automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external automation users use this skill to run a BrowserAct workflow that collects Google Trends interest data for market research, competitive monitoring, reporting, and dataset enrichment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill asks users to share a BrowserAct API key in chat.

Mitigation: Set BROWSERACT_API_KEY locally and do not paste the key into chat.

Risk: The security summary says the artifact documents broader, potentially sensitive scraping outputs than the stated Google Trends purpose requires.

Mitigation: Use the skill only for the named Google Trends BrowserAct workflow; avoid contact-data extraction or broad public-record scraping unless the skill is narrowed and redaction guidance is added.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/google-trends-interest-scraper-api-skill)
- [browseract-cli publisher profile](https://clawhub.ai/user/browseract-cli)
- [BrowserAct Console](https://www.browseract.com/reception/integrations?co-from=google-trends-interest-scraper)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime results are printed as JSON from the BrowserAct API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python and BROWSERACT_API_KEY; polls BrowserAct task status before printing results.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
