## Description:

Helps agents search, filter, aggregate, and retrieve records from Crawlora's pre-indexed public datasets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to answer population-level questions, find matching records, and inspect public hosted datasets without crawling individual source pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and parameters are sent to Crawlora and successful requests consume credits.

Mitigation: Use only for public dataset research, avoid private or secret lookup data, and monitor credit use.

Risk: Exposing the Crawlora API key in prompts, logs, or committed files could compromise the account.

Mitigation: Keep CRAWLORA_API_KEY in the environment and out of prompts, logs, and version control.

## Reference(s):

- [Crawlora datasets endpoint reference](reference/endpoints.md)
- [Crawlora Datasets ClawHub release](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown with optional JSON excerpts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dataset results may be paginated and reflect scheduled refreshes rather than live data.]

## Skill Version(s):

1.0.21 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
