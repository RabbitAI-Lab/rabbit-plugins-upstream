## Description:

Routes TikTok research requests through Gecho Bridge MCP to search videos, collect creator and video details, retrieve comments, and run product, trend, competitor, and content insight workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to conduct TikTok market and content research from an agent, including keyword search, creator collection, single-video detail and comment collection, asynchronous insight jobs, and status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow connects Gecho to a logged-in TikTok browser session.

Mitigation: Use it only when this access is acceptable for the user and keep TikTok and Gecho account sessions under user control.

Risk: TikTok research results may be saved locally and can include platform content, creator metadata, comments, or insight outputs.

Mitigation: Prefer a private save directory and delete saved result files when they are no longer needed.

Risk: The workflow depends on an external Chrome extension and npm package.

Mitigation: Review the Gecho extension and package before configuring MCP, and install them from the published Gecho links.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gecho-ai/skills/tiktok-search-zh-cn)
- [Gecho Website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome Extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw Configuration Video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes Configuration Video](https://www.youtube.com/watch?v=zHKnuWnxt_c)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, JSON files]

**Output Format:** [Markdown guidance with shell commands, structured result summaries, job IDs, status messages, and local JSON result paths when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May instruct the agent to call one Gecho TikTok MCP tool at a time and summarize only a limited subset of returned results.]

## Skill Version(s):

1.1.36 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
