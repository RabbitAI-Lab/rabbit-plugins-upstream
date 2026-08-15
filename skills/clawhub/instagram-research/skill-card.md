## Description:

Researches public Instagram profiles, posts, and Reels through the Crawlora API and returns normalized JSON for profile stats, post media and engagement, and Reels feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve public Instagram profile data, post details, and Reels feeds for influencer vetting, competitor social audits, brand monitoring, and post-level engagement checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call API paths beyond the Instagram endpoints described by the skill.

Mitigation: Use it only for the documented Instagram endpoints and add an Instagram-only allowlist before automated use.

Risk: Request bodies or parameters could expose secrets or unrelated private data to the Crawlora API.

Mitigation: Do not pass secrets or unrelated private data, keep the API key in CRAWLORA_API_KEY, and avoid hardcoding or committing credentials.

## Reference(s):

- [instagram-research endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Instagram endpoints for profiles, Reels, and post details.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
