## Description:

This skill helps users run the Career Site Job Listings Scraper BrowserAct template and extract structured public data from public company career pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to collect public career-page job listings for market research, competitive monitoring, dataset enrichment, reporting, and repeatable BrowserAct API automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to provide a BrowserAct API key directly to the agent.

Mitigation: Configure BROWSERACT_API_KEY through a secure environment or secret-management mechanism instead of pasting the key into chat.

Risk: The skill may activate for overly broad scraping requests.

Mitigation: Use it only for public career pages approved for BrowserAct processing and keep the target URL scoped to the intended company career site.

Risk: The supplied URL and extracted results are processed by BrowserAct.

Mitigation: Avoid submitting private, confidential, or unapproved URLs or data through the BrowserAct workflow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/career-site-job-listings-scraper-api-skill)
- [BrowserAct API Key Console](https://www.browseract.com/reception/integrations?co-from=career-site-job-listings-scraper)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; successful runs return the BrowserAct API response for downstream analysis.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
