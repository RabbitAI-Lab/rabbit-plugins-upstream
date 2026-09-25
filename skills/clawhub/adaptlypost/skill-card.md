## Description:

AdaptlyPost helps agents draft, schedule, publish, review, and analyze social posts through the AdaptlyPost API for connected social accounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an AdaptlyPost account use this skill to let an agent create drafts, schedule or publish posts, upload media, manage selected post workflows, and read analytics for connected social accounts. It is intended for social media operations where a human can confirm high-impact actions before the agent writes to the workspace.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or delete social posts and can manage account links and webhooks when the supplied token has sufficient authority.

Mitigation: Use a dedicated revocable token with the least role needed, prefer Contributor for draft-only workflows, and require explicit confirmation for live posts, deletions, webhook changes, media uploads, and connect-link actions.

Risk: Media uploads create public URLs, and connect links or webhook signing secrets can function like credentials.

Mitigation: Confirm the exact media file before upload, avoid broad local folders for media selection, share connect links only with the intended user, revoke links after use, and keep webhook secrets out of public channels, logs, and files.

## Reference(s):

- [AdaptlyPost ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform-Specific Configs Reference](references/platform-configs.md)
- [AdaptlyPost OpenClaw Plugin](https://github.com/adaptlypost/adaptlypost-openclaw/tree/main/openclaw-plugin)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, API calls, JSON]

**Output Format:** [Markdown guidance with inline curl commands and JSON request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADAPTLYPOST_API_KEY and curl; API actions operate on the user's connected AdaptlyPost workspace.]

## Skill Version(s):

1.8.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
