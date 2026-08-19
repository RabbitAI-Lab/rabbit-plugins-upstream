## Description:

Researches Apple job postings via the Crawlora API, searches jobs.apple.com, and retrieves full posting details such as description, qualifications, location, and team as normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and agents supporting job-market research use this skill to search Apple's public careers listings and retrieve full details for specific Apple requisitions or evergreen roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths and methods with the user's Crawlora API key.

Mitigation: Review generated commands before execution and prefer an allowlisted helper limited to /apple-jobs/search and /apple-jobs/job.

Risk: The skill requires CRAWLORA_API_KEY for authenticated API access.

Mitigation: Keep the key in the environment only, do not hardcode or commit it, and avoid passing it in query parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/apple-jobs-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; search results are metadata-only, and full posting details require a separate job detail call.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
