## Description:

Searches Google's public careers site (careers.google.com) via the Crawlora API and pulls single job postings by id, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and job researchers use this skill to search public Google Careers postings by role or location and retrieve full details for a specific numeric Google job id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to endpoints beyond the Google Jobs endpoints.

Mitigation: Review agent calls before execution and restrict use to /google-jobs/search and /google-jobs/job.

Risk: The skill requires a Crawlora API key that could be exposed if hardcoded or logged.

Mitigation: Provide the key only through CRAWLORA_API_KEY and avoid committing, echoing, or passing it in URLs.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/google-jobs-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Google Careers posting data.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
