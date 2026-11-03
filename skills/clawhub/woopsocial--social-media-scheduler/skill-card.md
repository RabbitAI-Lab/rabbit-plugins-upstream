## Description:

Schedule and publish social media posts to Facebook, Instagram, Threads, LinkedIn, LinkedIn Pages, X/Twitter, TikTok, Pinterest, and YouTube through WoopSocial's remote MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[woopsocial](https://clawhub.ai/user/woopsocial)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to configure WoopSocial's MCP server and have an agent schedule, publish, cross-post, draft, or inspect social media posts across connected accounts. It is suited for content-calendar and auto-publishing workflows where target accounts, content, media, and schedule are explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API-key URL setup method can expose credentials for accounts that can publish public posts.

Mitigation: Prefer OAuth setup, avoid placing API keys in MCP URLs where possible, and rotate any key that may have been exposed.

Risk: The skill can create, schedule, upload media for, and delete social-media resources when explicitly requested.

Mitigation: Review target accounts, content, media, schedule, and deletion intent carefully before public posting or destructive actions.

Risk: Post creation does not by itself prove that content was published successfully.

Mitigation: Check returned delivery state with WoopSocial and distinguish pending, scheduled, published, and failed states.

## Reference(s):

- [WoopSocial homepage](https://woopsocial.com)
- [WoopSocial documentation](https://docs.woopsocial.com)
- [WoopSocial dashboard API access](https://app.woopsocial.com/api-access)
- [ClawHub skill page](https://clawhub.ai/woopsocial/skills/social-media-scheduler)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post IDs, requested schedules, delivery states, account-selection guidance, and media-upload instructions returned through the WoopSocial MCP workflow.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
