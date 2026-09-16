## Description:

Researches Upwork job postings and freelancer profiles via the Crawlora API, returning normalized JSON for job searches, job detail lookups, and freelancer profile research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and marketplace researchers use this skill to search public Upwork job listings, inspect full job postings, estimate market rates from budgets, and review public freelancer profile signals before outreach or hiring decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Upwork search terms, job ids, freelancer ids, and the Crawlora API key to Crawlora's external API.

Mitigation: Use an authorized Crawlora API key, avoid sensitive or personal search text, and review Crawlora and Upwork terms for the intended use.

Risk: Returned job and freelancer data can influence hiring, pricing, or outreach decisions.

Mitigation: Treat the JSON output as research input, review relevant public source context, and apply human judgment before making decisions.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Upwork data through Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
