## Description:

Fetches a company's open roles from ATS-hosted career boards through the Crawlora API and returns normalized JSON for board listings, job detail, and hiring-velocity snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and recruiting researchers use this skill to retrieve public ATS job-board data for a known company board slug, inspect individual postings, compare role changes, or build hiring-signal snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths and methods beyond the ATS job-board endpoints.

Mitigation: Restrict automated use to the documented /jobs/* endpoints and review commands before sending job-query parameters or API credentials to Crawlora.

Risk: The skill requires a Crawlora API key and sends ATS slugs and job-query parameters to Crawlora.

Mitigation: Keep CRAWLORA_API_KEY in the environment, never hardcode or commit it, and use the skill only when sending the target research data to Crawlora is acceptable.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and ATS-specific company, board, or tenant slugs.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
