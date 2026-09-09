## Description:

Researches Instagram profiles, posts, and Reels via the Crawlora API, returning clean JSON for public profile stats, post media and engagement, or a user's Reels feed instead of scraping the app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve public Instagram profile stats, post media and engagement details, and Reels feeds through Crawlora for social audits, influencer vetting, brand monitoring, and post-level checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Bash helper can call broader Crawlora API paths than the Instagram endpoints described by the skill.

Mitigation: Review before installing, use only in trusted environments, and prefer restricting calls to the documented Instagram GET endpoints.

Risk: The helper allows CRAWLORA_API_BASE to override the default API base.

Mitigation: Remove the override or validate it strictly before use so authenticated requests are sent only to trusted endpoints.

Risk: The skill requires a Crawlora API key for authenticated requests.

Mitigation: Keep the key in CRAWLORA_API_KEY only and do not hardcode, log, query-param, or commit the secret.

## Reference(s):

- [Instagram endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/instagram-research)

## Skill Output:

**Output Type(s):** [JSON, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; public Instagram data only; Reels and post endpoints require a numeric Instagram user ID.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
