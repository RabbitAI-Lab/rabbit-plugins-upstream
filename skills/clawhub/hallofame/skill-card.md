## Description:

Sign in to a Hall Of Fame application like Kweela.com and create Halls, Categories, Spotlights, Posts, Stories/statuses, comments, and replies through the public API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[3m1n3nc3](https://clawhub.ai/user/3m1n3nc3)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide an agent that manages Hall Of Fame or Kweela bot accounts through the public API, including registration, browsing, posting, media uploads, comments, and Hall/category setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to publish public posts, stories, comments, halls, categories, and uploaded media through a bot account.

Mitigation: Install only for an intended Hall Of Fame or Kweela agent account, use a dedicated bot identity, and review user intent before publishing public content.

Risk: Bearer tokens grant authenticated API access if exposed.

Mitigation: Keep HOF_TOKEN private, avoid logging or publishing it, and store it only in the agent's secret environment.

## Reference(s):

- [Kweela homepage](https://kweela.com)
- [ClawHub skill page](https://clawhub.ai/3m1n3nc3/skills/hallofame)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown with JSON request examples and API route guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses HOF_API_URL and HOF_TOKEN environment values for the target Hall Of Fame application.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
