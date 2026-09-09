## Description:

Collect structured LinkedIn company information from one or more known company URLs. Do not use for personal profiles, jobs, or Crunchbase URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect structured Dataify results for known LinkedIn company URLs and related LinkedIn scraper-family tasks. It can prepare Builder requests, submit tasks with a Dataify token, wait for completion, and return final JSON results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact can invoke broader scraping workflows than the LinkedIn company URL description alone suggests.

Mitigation: Review intended scope before installing or running it, and avoid jobs, keyword scraping, Crunchbase, or broad discovery unless those capabilities are explicitly acceptable.

Risk: The skill uses a Dataify API token and may submit paid asynchronous tasks.

Mitigation: Use a dedicated, low-privilege Dataify token and confirm high-volume or multi-input requests before execution.

Risk: Task results and local raw output files may contain sensitive collected data.

Mitigation: Limit access to generated output directories and handle downloaded results according to the user's data retention and sharing requirements.

Risk: Persistent shell profile changes for token setup can outlive the immediate task.

Mitigation: Prefer session-scoped token configuration unless persistent environment changes are intentional and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-linkedin-company-information-by-url)
- [Tool parameter catalog](artifact/references/tool-params.json)
- [Dataify Builder endpoint](https://scraperapi.dataify.com/builder)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return summarized large payloads while preserving access to raw task results.]

## Skill Version(s):

1.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
