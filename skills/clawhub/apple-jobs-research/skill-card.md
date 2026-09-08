## Description:

Researches Apple job postings via the Crawlora API, searches jobs.apple.com, and pulls full posting detail including description, qualifications, location, and team as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, recruiters, and job-market researchers use this skill to search Apple's public careers listings and retrieve full details for specific Apple requisitions or pipeline roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to a configurable API destination through CRAWLORA_API_BASE.

Mitigation: Use a dedicated low-risk Crawlora key and keep CRAWLORA_API_BASE fixed to https://api.crawlora.net/api/v1.

Risk: Untrusted project files or wrappers could influence command arguments or the API base used by the helper.

Mitigation: Review commands before running them and avoid executing the helper in environments where untrusted files can set environment variables or wrap shell commands.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API credentials from CRAWLORA_API_KEY and returns normalized JSON from Apple Jobs search and job-detail endpoints.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
