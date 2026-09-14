## Description:

OpenClaw AdaptlyPost lets agents draft, schedule, publish, review, and analyze social posts through AdaptlyPost across Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest, and YouTube accounts connected to an AdaptlyPost token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with an AdaptlyPost account use this skill to create drafts, schedule or publish social content, upload approved media, list connected accounts, check delivery status, and review analytics for connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create public posts or retry failed posts on connected social accounts.

Mitigation: Confirm the exact content, target accounts, timing, and visibility before any write action; use drafts when the user is uncertain or no human can approve.

Risk: Uploaded media receives a public URL before a post is created.

Mitigation: Upload only user-named media from approved locations or public HTTPS URLs, review each file before upload, and prefer the OpenClaw plugin mediaDir controls.

Risk: The AdaptlyPost token can reach every social account in its connected account group.

Mitigation: Use a dedicated, revocable token and connect only the minimum accounts needed for the agent's task.

Risk: Connect links, upload URLs, webhook secrets, and live posting actions are sensitive.

Mitigation: Share secrets only with the requesting user, avoid logging them, review every approval prompt, and revoke connect links when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost Homepage](https://adaptlypost.com)
- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform-Specific Configs Reference](references/platform-configs.md)
- [OpenClaw Plugin README](openclaw-plugin/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON request and response examples, and OpenClaw tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADAPTLYPOST_API_KEY and curl for the skill workflow; OpenClaw plugin mode uses a configured apiToken and approval prompts for uploads, scheduling, live posting, and retries.]

## Skill Version(s):

1.6.1 (source: evidence release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
