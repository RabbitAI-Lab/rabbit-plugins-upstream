## Description:

Publish a social media post right now to one or more connected accounts (X, LinkedIn, Instagram, TikTok, Facebook, Threads, Bluesky, YouTube, Pinterest) through PostLake.

This skill is ready for commercial/non-commercial use.

## Publisher:

[postlake](https://clawhub.ai/user/postlake)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to publish immediate social media posts through PostLake to selected connected accounts or profiles, with per-target status reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Accidental live posting to connected social accounts.

Mitigation: Before calling the API, confirm the exact post text, media, profile or account IDs, platforms, and whether a selected profile expands to multiple live accounts.

Risk: Duplicate live posts during retries.

Mitigation: Send a unique Idempotency-Key header with every publish request so retries replay the same result instead of creating another post.

Risk: Incorrect interpretation of partial publishing outcomes.

Mitigation: Review and report each target's state and URL separately because one failed target does not prevent other selected platforms from publishing.

Risk: Platform-specific constraints can cause unexpected failures.

Mitigation: Check media requirements for Instagram, TikTok, YouTube, and Pinterest, and verify X entitlement before treating platform errors as skill failures.

## Reference(s):

- [PostLake publish skill page](https://clawhub.ai/postlake/skills/postlake-publish)
- [PostLake API base URL](https://api.postlake.dev)
- [PostLake create post endpoint](https://api.postlake.dev/v1/posts)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires POSTLAKE_API_KEY and a target profile or account list; responses include per-target state and URL.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
