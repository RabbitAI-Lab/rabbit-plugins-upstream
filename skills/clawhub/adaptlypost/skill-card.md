## Description:

Schedule, publish and review social posts through the AdaptlyPost API on Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest and YouTube accounts connected to AdaptlyPost, and read their analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing operators use this skill to manage social posts through an AdaptlyPost account group: list connected accounts, upload media, create drafts, schedule or publish posts, check delivery status, administer connect links and webhooks, and review analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish, schedule, retry, or delete social posts and these actions can affect public brand or personal accounts.

Mitigation: Require explicit human confirmation for each post, retry, publish, and delete action, including content, platform accounts, timing, and visibility; default unattended or uncertain workflows to drafts.

Risk: The skill can create account connect links and webhook registrations, expanding account administration beyond basic posting and analytics.

Mitigation: Create connect links or webhooks only when specifically requested, share connect URLs only with the intended user, store webhook secrets securely, verify webhook signatures, and revoke links or registrations when no longer needed.

Risk: The API token delegates access to every connected account in the AdaptlyPost account group.

Mitigation: Use a dedicated revocable API token, connect only the accounts required for the workflow, and keep ADAPTLYPOST_API_KEY out of logs, public channels, and non-AdaptlyPost hosts.

Risk: Uploaded media becomes publicly reachable through the returned public URL before a post is created or published.

Mitigation: Upload only user-named image or video files after confirming the exact path, avoid broad directories such as Downloads or Desktop unless confirmed per file, and refuse hidden files, credentials, configuration files, and documents.

## Reference(s):

- [AdaptlyPost Skill Page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API Reference](artifact/references/api-reference.md)
- [Platform-Specific Configs Reference](artifact/references/platform-configs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies and curl command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ADAPTLYPOST_API_KEY and curl for authenticated API calls; media uploads use user-named files and presigned upload URLs.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
