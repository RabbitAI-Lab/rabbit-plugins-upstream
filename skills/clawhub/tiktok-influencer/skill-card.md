## Description:

Collect public videos from a TikTok creator with Gecho Bridge MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gecho-ai](https://clawhub.ai/user/gecho-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect and summarize public TikTok creator video data, including captions, engagement metrics, publish times, creator metadata, and links. It is best suited for creator research, influencer review, and recent-post analysis through the Gecho Bridge MCP workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow depends on Gecho Bridge and the Gecho Chrome extension operating in a logged-in browser session.

Mitigation: Install only if you trust the publisher and keep TikTok login, CAPTCHA, verification, and region prompts under manual user control in Chrome.

Risk: Collected creator-video data may be saved to a local JSON file and could contain data the user does not intend to share.

Mitigation: Review generated local JSON files before sharing them and use the workflow only for creator profiles the user intends to collect.

Risk: Leaving the MCP entry or browser extension installed after use may preserve an integration the user no longer needs.

Mitigation: Remove the Gecho MCP entry or Chrome extension when the integration is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gecho-ai/skills/tiktok-influencer)
- [Gecho website](https://gecho.ai/)
- [Gecho Bridge README](https://github.com/gecho-ai/gecho-bridge/blob/main/README.md)
- [Gecho Chrome extension](https://chromewebstore.google.com/detail/pjkaeenpekolahdbccjfenjcmanemlbj?utm_source=item-share-cb)
- [OpenClaw setup video](https://www.youtube.com/watch?v=ggwY9hISHcQ)
- [Hermes setup video](https://www.youtube.com/watch?v=zHKnuWnxt_c)
- [Gecho YouTube channel](https://www.youtube.com/@Gecho-AI)
- [Gecho Discord support](https://discord.gg/RFDVZMR6Tn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with setup commands and summarized JSON-derived results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a saved local JSON result path when the Gecho MCP workflow writes collected creator-video data.]

## Skill Version(s):

1.1.36 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
