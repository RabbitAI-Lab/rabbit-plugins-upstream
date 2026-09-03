## Description:

Schedule and manage social media posts across Instagram, X (Twitter), Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest, and YouTube using the AdaptlyPost API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent draft, schedule, publish, inspect, and retry social media posts across connected AdaptlyPost accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can publish or schedule public, attributable social media content on connected accounts.

Mitigation: Use a dedicated revocable token, connect only needed accounts, and require explicit confirmation of content, platforms, timing, and visibility before each post.

Risk: Media uploaded for posting may become externally reachable.

Mitigation: Upload only user-named files or approved public URLs, and confirm the user is comfortable making that media reachable before upload.

Risk: Failed or skipped platform publishes can lead to duplicate or unwanted retry behavior.

Mitigation: Surface skipped platforms and errors to the user, honor rate-limit guidance, and retry only after the cause is understood and approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform-Specific Configs Reference](references/platform-configs.md)
- [OpenClaw Plugin Manifest](openclaw-plugin/openclaw.plugin.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADAPTLYPOST_API_KEY and connected social accounts; write actions may publish or schedule public social content.]

## Skill Version(s):

1.0.11 (source: evidence.release.version; source skill frontmatter reports 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
