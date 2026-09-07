## Description:

Lists a WeChat Channels author's posts by account ID or share link, including titles, publish times, object IDs, and optional share links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dunkong](https://clawhub.ai/user/dunkong)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content operators use this skill to review recent posts from a specific WeChat Channels author and export the results for tracking, reporting, or content inventory work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends API keys and queried WeChat Channels data to api.we-media.cn.

Mitigation: Install only when the publisher and service are trusted; use a dedicated low-privilege API key and review config.json, generated output files, and the local cache for sensitive content.

Risk: The artifact includes under-disclosed paths that can upload local files when --file or local videoUrl/audioUrl values are passed.

Mitigation: Do not allow local file arguments unless the user intentionally wants those files uploaded to remote temporary storage; inspect commands before adding --yes.

Risk: The release ships Python bytecode cache files.

Mitigation: Remove shipped __pycache__ files before install or execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dunkong/skills/wechat-channel-author-feed)
- [We-Media API service](https://api.we-media.cn)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files, Markdown, JSON, Configuration]

**Output Format:** [Markdown guidance with inline shell commands; runtime results can be written as Markdown, JSON, or Excel files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a We-Media API key. Paid calls require explicit user confirmation, and successful paid POST responses may be cached locally for 24 hours.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
