## Description:

Researches X (formerly Twitter) profiles and posts via the Crawlora API, returning clean JSON for public profile stats, recent posts, and single-post content and engagement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve normalized JSON about public X profiles, recent posts, and individual posts for social-listening, competitor research, and post-level checks without browser automation or official X API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script is broader than the X-only skill description and can call arbitrary Crawlora API paths with the user's API key.

Mitigation: Review generated commands before execution and restrict use to the documented X endpoints: /x/profile/{username}, /x/profile/{username}/posts, and /x/post/{id}.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed in logs.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid echoing it in commands or logs, and rotate the key if exposure is suspected.

Risk: The skill works only with public X profiles and posts and depends on third-party API behavior and terms.

Mitigation: Use the skill only for public data, respect applicable X and Crawlora terms, and verify important results against source material before relying on them.

## Reference(s):

- [x-research ClawHub skill page](https://clawhub.ai/tonywangcn/skills/x-research)
- [x-research endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API requests; documented X profile-post results are limited to the first public page payload.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
