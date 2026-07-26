## Description: <br>
China News Tool Free helps agents retrieve Chinese news from RSS feeds, classify items by topic, and generate lightweight news briefs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to collect RSS-based Chinese news from configured public feeds, categorize items, and produce local daily briefs for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Activation metadata is broader than the free RSS news purpose and may cause use for generic LLM, dialogue, or agent orchestration tasks. <br>
Mitigation: Limit invocation to RSS-based Chinese news retrieval and local brief generation, and review the skill before installation or automation. <br>
Risk: RSS content and keyword categorization can be incomplete, unavailable, stale, or misclassified. <br>
Mitigation: Review generated briefs before use, refresh RSS URLs when feeds fail, and adjust category keywords for the intended topics. <br>
Risk: Artifact examples include shell and Python execution plus local file writes. <br>
Mitigation: Inspect commands before execution, run in a constrained workspace, and control output and cache directories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/china-news-tool-free) <br>
- [Sina China RSS feed](https://rss.sina.com.cn/news/china/roll.xml) <br>
- [Sina World RSS feed](https://rss.sina.com.cn/news/world/roll.xml) <br>
- [Sohu News RSS feed](https://news.sohu.com/rss/) <br>
- [36Kr RSS feed](https://36kr.com/feed) <br>
- [Phoenix News RSS feed](https://news.ifeng.com/rss/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown briefs, text status output, Python code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local Markdown or JSON cache files such as news_<date>.md when the agent follows the artifact examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
