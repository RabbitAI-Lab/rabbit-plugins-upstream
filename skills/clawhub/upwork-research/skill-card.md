## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, returning normalized JSON for job search, job detail, freelancer profile lookup, rate checks, and freelancer vetting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and hiring teams use this skill to research public Upwork jobs and freelancer profiles, estimate market rates, and review freelancer history before outreach or hiring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Upwork search terms, job IDs, freelancer IDs, and the Crawlora API key to Crawlora.

Mitigation: Use it only for intended public Upwork research, keep CRAWLORA_API_KEY in the environment, and avoid private Upwork pages or account data.

Risk: Undocumented API routes or methods could broaden what the helper sends.

Mitigation: The included helper is limited to documented GET routes for Upwork search, job detail, and freelancer profile lookup.

Risk: API keys can leak through command history or process listings if passed as arguments.

Mitigation: The helper reads CRAWLORA_API_KEY from the environment and supplies it to curl through a private temporary config file.

## Reference(s):

- [Upwork endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/upwork-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GET requests to documented Crawlora Upwork endpoints and prints raw JSON suitable for jq.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
