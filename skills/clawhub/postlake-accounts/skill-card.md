## Description:

List the social accounts connected to PostLake (X, LinkedIn, Instagram, TikTok, Facebook, Threads, Bluesky, YouTube, Pinterest) and their status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill before publishing through PostLake to list connected social accounts, confirm account IDs, and identify accounts that need reauthorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes connected account IDs, platform handles, and account status to the agent.

Mitigation: Install only when the agent needs to inspect PostLake account connections, and keep POSTLAKE_API_KEY scoped and protected.

Risk: An account with status "needs_reauth" cannot be used until it is reconnected.

Mitigation: Skip accounts that need reauthorization and direct the user to reconnect them in PostLake before posting.

## Reference(s):

- [PostLake skill page](https://clawhub.ai/postlake/skills/postlake-accounts)
- [PostLake publisher profile](https://clawhub.ai/user/postlake)
- [PostLake API base URL](https://api.postlake.dev)
- [PostLake API keys](https://app.postlake.dev/app/keys)
- [PostLake connected channels](https://app.postlake.dev/app/channels)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses POSTLAKE_API_KEY for authenticated account lookup; public platform capability checks do not require authentication.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
