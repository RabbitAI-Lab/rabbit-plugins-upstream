## Description:

Researches Tesla job postings via the Crawlora API by searching Tesla's careers site by title, department, or location and retrieving a single posting's full description by id as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and recruiting analysts use this skill to search public Tesla job listings and retrieve full posting details by job id. It helps answer role, department, and location questions using the documented Crawlora Tesla Jobs endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora endpoints and send arbitrary request bodies, beyond the documented Tesla Jobs endpoints.

Mitigation: Use the skill only with /tesla-jobs/list and /tesla-jobs/job, and add an endpoint and method allowlist before installation if strict Tesla-only behavior is required.

Risk: Secrets or personal data could be exposed if placed in query strings, request bodies, command history, or committed files.

Mitigation: Keep the Crawlora key in CRAWLORA_API_KEY only, avoid sending secrets or personal data in requests, and review commands before execution.

## Reference(s):

- [Tesla Jobs endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tesla-jobs-research)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public Tesla job-posting data and requires CRAWLORA_API_KEY for API access.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
