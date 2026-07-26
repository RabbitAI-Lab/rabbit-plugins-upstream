## Description: <br>
Fetches articles from WeChat, Xiaohongshu, Douban, and Zhihu, uploads article images to Aliyun OSS, extracts tags with an optional LLM, and archives results to Obsidian or optional Notion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ajayhao](https://clawhub.ai/user/ajayhao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to capture supported Chinese content-platform articles and save structured knowledge-base records in Obsidian, Notion, or terminal preview workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Aliyun OSS credentials and can use Notion and LLM API credentials when those integrations are enabled. <br>
Mitigation: Use limited-scope OSS and Notion credentials, configure only needed integrations, and keep API keys in the local agent environment. <br>
Risk: When LLM tag extraction is enabled, article text is sent to the configured LLM endpoint. <br>
Mitigation: Disable the LLM integration for sensitive content or avoid sending private, regulated, or confidential articles to the configured endpoint. <br>
Risk: Platform cookies may be used for WeChat or Zhihu fallback fetching. <br>
Mitigation: Use low-risk platform cookies and rotate or revoke them if they are no longer needed. <br>
Risk: The security guidance recommends upgrading the pinned lxml dependency before routine use. <br>
Mitigation: Review and update the pinned dependency set during deployment maintenance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ajayhao/skills/article-fetcher) <br>
- [Project homepage](https://github.com/AjayHao/article-fetcher) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files] <br>
**Output Format:** [Markdown files, Notion pages, and terminal text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload article images to Aliyun OSS and optionally create Notion pages when configured.] <br>

## Skill Version(s): <br>
1.3.4 (source: server release metadata, SKILL.md metadata, CHANGELOG v1.3.4 released 2026-07-19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
