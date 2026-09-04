## Description:

Collect structured Crunchbase company profiles from one or more known company URLs. Do not use for general web research or LinkedIn company URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit Dataify Builder requests for Crunchbase company collection, monitor the asynchronous task, and return the collected result. It is intended for known Crunchbase company URLs or the listed Crunchbase keyword tool, not broad web research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company URLs, keywords, and task parameters are sent to Dataify for Crunchbase collection.

Mitigation: Install and use the skill only when Dataify processing of those inputs is intended.

Risk: DATAIFY_API_TOKEN is required for authenticated requests.

Mitigation: Store the token using normal secret-management practices and do not paste it into chat or rendered outputs.

## Reference(s):

- [Tool parameter catalog](references/tool-params.json)
- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-crunchbase-company-by-url)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a task ID and resume command if monitoring times out or is interrupted.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
