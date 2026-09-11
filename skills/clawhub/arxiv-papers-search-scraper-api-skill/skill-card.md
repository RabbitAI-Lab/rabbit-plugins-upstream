## Description:

Runs a BrowserAct arXiv paper-search template and returns structured public arXiv paper metadata for research, monitoring, reporting, or downstream automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and automation users use this skill to run a BrowserAct workflow that searches arXiv and returns structured paper records for analysis, reporting, dataset enrichment, or downstream application workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User inputs and search parameters are sent to a third-party BrowserAct account.

Mitigation: Use the skill only with public, non-sensitive arXiv search terms and avoid proprietary or confidential queries.

Risk: The BrowserAct API key could be exposed if pasted into chat or stored insecurely.

Mitigation: Provide BROWSERACT_API_KEY through an environment variable or secret store and rotate it if exposure is suspected.

Risk: The skill description is broader than its arXiv paper-search purpose.

Mitigation: Restrict use to arXiv searches unless the publisher narrows and validates any broader scraping behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/arxiv-papers-search-scraper-api-skill)
- [browseract-cli publisher profile](https://clawhub.ai/user/browseract-cli)
- [BrowserAct Console](https://www.browseract.com/reception/integrations?co-from=arxiv-papers-search-scraper)
- [arXiv](https://arxiv.org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-formatted API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; polls BrowserAct task status and prints returned structured paper metadata when available.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
