## Description:

帮助内容运营、品牌调研人员和创作者围绕小红书关键词检索内容样本、拆解热门选题并规划内容角度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content operators, and brand researchers use this skill to search Xiaohongshu topics by keyword, collect representative notes, and organize evidence-backed topic angles for follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches are sent to SocialDataX and may reflect sensitive research intent.

Mitigation: Use non-sensitive queries when possible and confirm the user is comfortable sharing the search terms with SocialDataX.

Risk: Outputs and saved results may contain full tokenized Xiaohongshu URLs.

Mitigation: Review or sanitize saved and shared results before broader distribution when tokenized URLs are not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-topic-analysis-v2)
- [SocialDataX AI homepage](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and Xiaohongshu search result summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include full tokenized Xiaohongshu note URLs when returned by the data source; requires SOCIALDATAX_API_KEY and a Node.js/npm-capable environment.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
