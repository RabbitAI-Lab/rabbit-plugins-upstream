## Description: <br>
小红书内容搜索工具。通过 browser 工具操控已登录的 Chrome，搜索小红书公开笔记，提取标题、正文、话题标签、点赞数，分析消费趋势。用于市场调研中的消费者趋势研究。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amostafoya-pixel](https://clawhub.ai/user/amostafoya-pixel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Market research users and business planning agents use this skill to search public Xiaohongshu notes, extract post metadata and content, and summarize consumer trend signals for commercial research reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks an agent to control a logged-in Chrome session through local remote debugging. <br>
Mitigation: Use a separate Chrome profile or test account, keep remote debugging local, close the browser when finished, and avoid profiles with unrelated sensitive logins. <br>
Risk: Extracted public social content and trend summaries may be incomplete or misleading if used without review. <br>
Mitigation: Review extracted notes, links, and synthesized insights before adding them to business research deliverables. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/amostafoya-pixel/xiaohongshu-search) <br>
- [Xiaohongshu search result example](https://www.xiaohongshu.com/search_result?keyword=2025消费趋势&source=web_explore_feed) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with browser command examples and trend analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include note titles, links, author names, like counts, extracted note content, topic tags, and synthesized trend insights.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
