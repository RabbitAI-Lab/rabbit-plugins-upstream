## Description: <br>
用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content researchers, analysts, and social media teams use this skill to retrieve Weibo hot-search rankings and keyword-based post results for trend scanning, competitor analysis, and content research. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Weibo research queries and the SocialDataX API key to SocialDataX's hosted service. <br>
Mitigation: Install only when this data sharing is intended, keep SOCIALDATAX_API_KEY in the runtime environment, and avoid pasting API keys into chat, logs, or screenshots. <br>
Risk: The documented direct CLI uses the external npm package at @latest, so future package updates may change runtime behavior. <br>
Mitigation: Use a pinned package version or controlled installer when reproducibility matters, and review updates before deployment. <br>


## Reference(s): <br>
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown summaries with command examples and selected JSON fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Weibo ranking signals, post IDs, URLs, author facts, interaction counts, publish times, and pagination markers for traceability.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
