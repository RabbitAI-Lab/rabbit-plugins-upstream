## Description:

Researches social-media profiles, posts, and engagement across Instagram, TikTok, Threads, Bluesky, X, Pinterest, LinkedIn, Facebook, and Reddit via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, marketers, and social-media analysts use this skill to look up public profiles, posts, engagement, searches, trends, competitor activity, and brand mentions across supported social platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths and HTTP methods beyond the documented social-media scope.

Mitigation: Use the skill only with non-sensitive public research targets, and add endpoint and method allowlisting before treating the helper as a constrained wrapper.

Risk: Queries go to Crawlora under the user's API key.

Mitigation: Keep CRAWLORA_API_KEY in the environment only, avoid hardcoding or committing it, and do not send sensitive research targets.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/social-media-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Crawlora API and returns normalized JSON from public social-media endpoints.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
