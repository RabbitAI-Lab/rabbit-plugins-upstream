## Description:

Schedules, publishes, reviews, and analyzes social posts through AdaptlyPost across Instagram, X, Bluesky, TikTok, Threads, LinkedIn, Facebook, Pinterest, and YouTube accounts connected to the user's AdaptlyPost account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent draft, schedule, publish, retry, inspect, and analyze social posts for AdaptlyPost-connected accounts. It is intended for users who already have an AdaptlyPost account, an API token, and connected social accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved agent actions can publish posts or uploaded media publicly through connected social accounts.

Mitigation: Use a dedicated revocable API token, connect only the accounts the agent needs, and review every approval prompt before upload, scheduling, publishing, or retry.

Risk: Unattended or uncertain workflows may publish content without timely human review.

Mitigation: Default uncertain or unattended runs to drafts, and require fresh confirmation before changing a draft-only workflow into live posting.

Risk: Media uploads can expose unintended local files or unsafe URL downloads.

Mitigation: Keep upload folders narrow, confirm exact media paths, avoid broad folders, and allow only public HTTPS media URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tarasshyn/skills/adaptlypost)
- [Publisher profile](https://clawhub.ai/user/tarasshyn)
- [AdaptlyPost homepage](https://adaptlypost.com)
- [AdaptlyPost API Reference](references/api-reference.md)
- [Platform-Specific Configs Reference](references/platform-configs.md)
- [OpenClaw plugin README](openclaw-plugin/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with curl commands, JSON request bodies, and OpenClaw plugin tool instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ADAPTLYPOST_API_KEY and curl for the skill path; the OpenClaw plugin requires an apiToken and may restrict local uploads with mediaDirs.]

## Skill Version(s):

1.1.2 (source: server release metadata; artifact frontmatter reports 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
