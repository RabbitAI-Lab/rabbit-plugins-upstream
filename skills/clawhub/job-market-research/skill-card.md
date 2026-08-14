## Description:

Researches job postings, hiring signals, and freelance gigs via the Crawlora API -- Indeed, Google/Amazon/Apple/Meta/Tesla careers sites, any company's ATS board (Greenhouse, Lever, Workday, SmartRecruiters, Ashby, and more), plus Upwork and Fiverr -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, analysts, and other external users can use this skill to search job postings, inspect company hiring activity, aggregate hiring signals, and research freelance gigs or sellers through Crawlora API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can use the Crawlora API key against Crawlora endpoints beyond the job-market paths described by the skill.

Mitigation: Use a constrained wrapper or require explicit user confirmation for each request path before the agent executes API calls.

Risk: API calls may consume Crawlora account credits.

Mitigation: Review planned queries and pagination before execution, and monitor usage under the configured Crawlora account.

Risk: The skill depends on an API key stored in the CRAWLORA_API_KEY environment variable.

Mitigation: Provide the key only through the environment and do not hardcode, log, or commit it.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/job-market-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated public job-market or freelance data from Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
