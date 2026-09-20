## Description:

Researches X (formerly Twitter) profiles and posts via the Crawlora API, returning clean JSON for public profile stats, recent posts, or single-post content and engagement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve normalized public X profile, timeline, and post-detail JSON through Crawlora instead of scraping x.com or using the official X API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public X lookup requests to Crawlora as a third-party service.

Mitigation: Install only if comfortable using Crawlora for public X lookups and review Crawlora and X terms before relying on returned data.

Risk: The Crawlora API key could be exposed if copied into prompts, command arguments, source files, or logs.

Mitigation: Keep CRAWLORA_API_KEY private, provide it through the environment, and do not hardcode or commit it.

Risk: Query values may reveal sensitive research interests or private context to a third-party service.

Mitigation: Do not pass private or sensitive information as query values.

## Reference(s):

- [x-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub x-research skill page](https://clawhub.ai/crawlora-org/skills/x-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON returned from Crawlora API calls, with Markdown guidance and inline shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and only supports documented GET routes for public X profile, profile-post, and post-detail lookups.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
