## Description: <br>
Batch-fetches detailed TikTok video performance and commerce metrics for known video IDs or URLs, including views, engagement, creator data, sales estimates, GMV estimates, and video attributes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, sellers, marketers, and agents use this skill to compare known TikTok videos side by side by playback, engagement, creator, commerce, and attribution metrics. It is intended for lookup and analysis of supplied video IDs or URLs, not discovery of new videos. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends TikTok video IDs or URLs, the LinkFox API key, and session or app metadata to LinkFox services. <br>
Mitigation: Install and run it only when that data sharing is acceptable for the user's task and environment. <br>
Risk: Full API responses are saved locally and may contain detailed TikTok analytics or operational context. <br>
Mitigation: Review local output directories and retention practices before using the saved JSON files in shared workspaces. <br>
Risk: Automatic feedback reporting can send user comments or operational context to a separate LinkFox feedback endpoint. <br>
Mitigation: Review or disable feedback reporting if that information should not be reported outside the active workflow. <br>
Risk: Video sales, GMV, and attribution values are estimates rather than exact TikTok platform figures. <br>
Mitigation: Present these fields as approximate analytics and avoid using them as the sole basis for financial decisions. <br>


## Reference(s): <br>
- [EchoTik batch video detail API reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-batch-video-detail) <br>
- [LinkFox tool gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON files, Guidance] <br>
**Output Format:** [Markdown summaries and comparison tables, with full JSON responses saved to local files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local cache hits, saved response paths, summarized large responses, and cost-token information.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
