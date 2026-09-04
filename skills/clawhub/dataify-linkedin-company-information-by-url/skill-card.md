## Description:

Collect structured LinkedIn company information from one or more known company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare authenticated Dataify Builder requests for known LinkedIn company URLs and return the collected result.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is advertised for LinkedIn company-URL collection but also exposes LinkedIn job-scraping options through an authenticated Dataify workflow.

Mitigation: Install only when the broader LinkedIn scraper family is intended, and review the selected Dataify tool before execution.

Risk: Permanent API-token setup can retain credentials beyond the immediate task.

Mitigation: Prefer session-scoped DATAIFY_API_TOKEN configuration unless a persistent shell variable is deliberately required.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with inline shell commands and JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a Dataify task ID and resume command if asynchronous monitoring times out or is interrupted.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
