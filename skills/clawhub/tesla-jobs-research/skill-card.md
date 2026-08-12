## Description:

Researches Tesla job postings via the Crawlora API by searching Tesla careers listings by title, department, or location and retrieving full posting details by job id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public Tesla job openings, inspect hiring activity by role or location, and retrieve full responsibilities and requirements for a specific posting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora endpoints beyond the Tesla jobs endpoints, which may expose the user's API key to unintended requests.

Mitigation: Review before installing and limit or edit the helper so it only calls /tesla-jobs/list and /tesla-jobs/job.

Risk: Search fields and API requests may include personal or sensitive information.

Mitigation: Use a Crawlora key appropriate for this tool and avoid placing sensitive personal data in query or location parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/tesla-jobs-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY. List results are metadata-only and paginated; full posting details require a follow-up job lookup.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
