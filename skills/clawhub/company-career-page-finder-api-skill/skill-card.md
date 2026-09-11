## Description:

This skill helps users run the Company Career Page Finder BrowserAct template and extract structured public data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[browseract-cli](https://clawhub.ai/user/browseract-cli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to run a BrowserAct career-page lookup for a company website and collect structured public career-page data for enrichment, reporting, or monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the target company website and task metadata to BrowserAct.

Mitigation: Use it only when sharing that task data with BrowserAct is acceptable.

Risk: The artifact tells users to provide an API key through chat when the environment variable is missing.

Mitigation: Configure BROWSERACT_API_KEY locally through a secure environment or secret manager, and rotate the key if it has already been shared.

Risk: Returned public web data can be incomplete, stale, or missing expected fields.

Mitigation: Ground conclusions in returned data and source URLs, handle missing fields gracefully, and review important results before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/company-career-page-finder-api-skill)
- [browseract-cli publisher profile](https://clawhub.ai/user/browseract-cli)
- [BrowserAct API key setup](https://www.browseract.com/reception/integrations?co-from=company-career-page-finder)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API response text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python and BROWSERACT_API_KEY; task polling can run for several minutes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
