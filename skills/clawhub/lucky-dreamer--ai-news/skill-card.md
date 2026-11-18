## Description:

Fetch and summarize the latest AI news from ai.codefather.cn/news (鱼皮AI导航 AI资讯) into a detailed, theme-grouped daily digest with per-article summaries and source links. Use this skill whenever the user asks for AI news, AI 日报, 最新 AI 资讯, 每日 AI 新闻, an AI news roundup, or wants to scrape/summarize AI-industry news from ai.codefather.cn / 鱼皮AI导航 for the latest or a specific date — even if they don't say "skill" or name the site, as long as the request is about collecting and summarizing AI news from ai.codefather.cn / 鱼皮AI导航.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lucky-dreamer](https://clawhub.ai/user/lucky-dreamer)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an assistant for current or date-specific AI news; the assistant collects articles from ai.codefather.cn, combines duplicate coverage, and returns a theme-grouped digest with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill fetches content over the network and writes article data and digest files; the security summary notes an undeclared tool scope.

Mitigation: Review its network and file-writing scope before use, and direct generated files to an intended output directory.

Risk: The security analysis reports incomplete reference checks, so its benign verdict does not confirm that every relevant detail was checked.

Mitigation: Review the skill and any unresolved references before deployment; treat the verdict as limited to the analysis that was completed.

## Reference(s):

- [鱼皮 AI 导航 · AI 资讯](https://ai.codefather.cn/news)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Theme-grouped AI news digest in Markdown, with structured article data in JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-article source links; output files can be written to a selected directory.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
