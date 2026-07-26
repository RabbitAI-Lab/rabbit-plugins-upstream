## Description: <br>
Analyze TikTok creators, TikTok Shop commerce, content, live streams, trends, ads, products, shops, categories, videos, hashtags, music, comments, and audience signals through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to route TikTok creator, commerce, content, live, trend, and ad-intelligence questions into documentation-guided KeyAPI REST workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and uses a KeyAPI token for live TikTok analytics requests. <br>
Mitigation: Treat the KeyAPI token as sensitive, keep it local, and review the shell-profile managed block created during setup. <br>
Risk: Queries, selected files, or image uploads may be transmitted to KeyAPI during requested API workflows. <br>
Mitigation: Use file upload and raw-output options only for data the user intends to transmit or save. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xyzzero/skills/keyapi-tiktok) <br>
- [KeyAPI Docs Index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Bearer Authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Rules](references/global-rules.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Scenarios](references/scenarios.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>
- [TikTok Rules](references/tiktok-rules.md) <br>
- [TikTok Search Module Rules](references/tiktok-search-rules.md) <br>
- [TikTok Shop Rules](references/tiktok-shop-rules.md) <br>
- [TikTok Influencer Module Rules](references/tiktok-influencer-rules.md) <br>
- [TikTok Content Composite Rules](references/tiktok-content-rules.md) <br>
- [TikTok Intelligence Module Rules](references/tiktok-intelligence-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce live API call plans, setup commands, analytical summaries, tables, raw JSON, or saved result files when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
