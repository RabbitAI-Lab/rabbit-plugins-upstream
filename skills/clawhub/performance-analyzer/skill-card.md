## Description: <br>
Analyzes influencer campaign performance by scoring results against targets and benchmarks, ranking platforms, creators, and content, reading engagement quality and sentiment, breaking down conversion attribution, and producing ranked learnings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, agencies, and creator-program operators use this skill during or after influencer campaigns to compare creator, platform, content, engagement, and conversion performance. It turns user-provided analytics, reports, benchmarks, and optional YouTube metrics into a structured performance analysis and recommendations for future campaign planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Campaign analytics, sales summaries, promo-code data, and influencer reports can expose sensitive business or customer information. <br>
Mitigation: Provide only the minimum needed data, prefer aggregated exports, and avoid customer-level records. <br>
Risk: Optional YouTube metric collection may require an API key. <br>
Mitigation: Configure API keys through the host's normal secret or environment-variable mechanism rather than pasting credentials into chat. <br>
Risk: Incomplete or statistically weak campaign data can lead to overconfident winner, loser, or roster recommendations. <br>
Mitigation: Review the analysis before acting, keep measured and user-provided data labels distinct, and mark low-confidence comparisons as keep-testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/performance-analyzer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Analysis templates](references/analysis-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown performance report with scorecards, comparison tables, attribution notes, and ranked recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the analysis to memory/influencer/performance-analyzer/YYYY-MM-DD-<campaign>.md and promote durable learnings to memory/hot-cache.md when the host supports canonical state.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
