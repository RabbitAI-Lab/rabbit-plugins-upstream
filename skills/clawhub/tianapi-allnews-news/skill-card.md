## Description: <br>
Fetches categorized news from TianAPI by channel ID for finance, sports, entertainment, technology, and other news categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workxin](https://clawhub.ai/user/workxin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve and summarize current news items from TianAPI categories by selecting a channel ID and optional result limits. It is intended for agent workflows that need category-based news lookup with source, timestamp, and article-link output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a TianAPI key for external HTTPS requests, and passing credentials on the command line or logging full request URLs can expose the key. <br>
Mitigation: Prefer a protected environment variable or carefully controlled .env file, and avoid sharing command history or logs that include full TianAPI request URLs. <br>
Risk: The release metadata documents TIANAPI_ALLNEWS_NEWS_KEY, while the packaged script reads TIANAPI_KEY. <br>
Mitigation: Set TIANAPI_KEY for the packaged script or update the wrapper before deployment so the documented and runtime environment variables match. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/workxin/skills/tianapi-allnews-news) <br>
- [TianAPI category news API](https://www.tianapi.com/apiview/51) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and plain-text or JSON-like news results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a TianAPI key; the server evidence notes that the packaged script reads TIANAPI_KEY.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
