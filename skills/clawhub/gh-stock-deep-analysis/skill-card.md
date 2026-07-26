## Description: <br>
gh-stock-deep-analysis guides agents through deep stock analysis for A-share, Hong Kong, and U.S. equities using a structured multi-dimensional framework. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ghgh2026](https://clawhub.ai/user/ghgh2026) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to prompt an agent to gather current market, financial, news, announcement, and research-report data for stock-analysis reports. The skill is intended to produce sourced markdown analysis with ratings, valuation discussion, risk notes, and a non-advice disclaimer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stock analyses may create local records, publish Feishu/Wiki documents, and notify a fixed chat group without clear user control. <br>
Mitigation: Require explicit user confirmation before saving, publishing, or messaging, and disable or remove those integrations unless the user expects that workflow. <br>
Risk: Broad triggers may activate the skill for short stock names, tickers, or generic analysis requests. <br>
Mitigation: Narrow activation to explicit stock-analysis requests before deployment. <br>
Risk: Generated reports include target prices, stop-loss levels, position sizing, and investment ratings. <br>
Mitigation: Keep the non-advice disclaimer, require dated sources for material claims, and route outputs through human financial review before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ghgh2026/skills/gh-stock-deep-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables, cited data points, ratings, and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local report records and publish or notify through configured Feishu/Wiki and chat integrations when those integrations are available.] <br>

## Skill Version(s): <br>
1.1.6 (source: server release metadata; artifact files contain 1.1.2, 1.1.5, and 1.1.8 internal version references) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
