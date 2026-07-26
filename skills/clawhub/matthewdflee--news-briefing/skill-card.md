## Description: <br>
Automated daily news briefing system that fetches Twitter/X posts, generates star-rated summaries, and delivers them via Feishu/Lark. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matthewdflee](https://clawhub.ai/user/matthewdflee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to set up a scheduled Twitter/X news digest that summarizes selected accounts and sends a concise daily briefing through Feishu/Lark. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow depends on a raw Twitter/X browser session token. <br>
Mitigation: Store TWITTER_AUTH_TOKEN only in a protected environment variable or secret store, rotate it periodically, and never paste it into chat logs or committed files. <br>
Risk: Briefing content and metadata may be sent to Feishu/Lark. <br>
Mitigation: Confirm that forwarding summarized posts, account metadata, and trading-related notes to Feishu/Lark is permitted by the user's data handling policies before enabling the automation. <br>
Risk: Fetched social media content can be incomplete, stale, duplicated, or misleading. <br>
Mitigation: Review high-impact briefing items before acting on them, keep deduplication state enabled, and treat trading-impact language as informational rather than financial advice. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/matthewdflee/skills/news-briefing) <br>
- [Information Source Configuration](artifact/references/sources.md) <br>
- [Adding New Bloggers](artifact/references/add-blogger.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown briefing text with setup commands, JSON state files, YAML configuration, and Feishu/Lark send commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces concise star-rated briefing content, optional tweet JSON output, and local state updates for deduplication and daily send tracking.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
