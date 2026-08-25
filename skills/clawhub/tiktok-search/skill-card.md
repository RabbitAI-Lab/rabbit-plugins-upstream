## Description:

Search TikTok videos, collect creator videos, retrieve detail data and comments for one known video, and run product, trend, competitor, and content insights through Gecho Bridge MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route TikTok research requests through Gecho Bridge MCP for keyword search, creator video collection, single-video detail and comment retrieval, and asynchronous product, trend, competitor, or content insight jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external Gecho MCP server and Chrome extension running against a logged-in TikTok browser session.

Mitigation: Install it only when the publisher and external runtime are trusted, and use it with accounts and browser sessions appropriate for the intended research task.

Risk: Collected TikTok metadata, comments, and replies may be saved as local JSON files.

Mitigation: Choose a safe save directory and review or delete saved result files when they are no longer needed.

Risk: The setup commands use an @latest external package, so runtime behavior may change outside this skill artifact.

Mitigation: Review the external package before deployment and consider pinning or validating updates in managed environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-search)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Setup Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Setup Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, configuration snippets, status summaries, and bounded summaries of JSON-like tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference saved local JSON result files produced by Gecho MCP tools; successful responses summarize results rather than pasting full raw data.]

## Skill Version(s):

1.1.37 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
