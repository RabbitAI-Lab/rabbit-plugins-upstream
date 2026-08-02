## Description: <br>
A WeChat Official Account copywriting skill that searches RedFox viral article data by keyword, analyzes high-performing content patterns, and generates publish-ready public-account articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuanyi-github](https://clawhub.ai/user/yuanyi-github) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Official-account owners, content operators, MCN teams, and brand planners use this skill to research recent WeChat viral articles, extract title and content patterns, and generate complete Chinese WeChat articles with recommended titles, a core viewpoint, tags, and formula-source analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports that the release ships a plaintext RedFox API key and should be treated as suspicious. <br>
Mitigation: Treat any bundled plaintext key as compromised, remove it before reuse, rotate the credential, and configure a revocable REDFOX_API_KEY through the runtime environment. <br>
Risk: The skill asks users for personal writing samples to adapt style, which may expose sensitive business topics or private diary-style content. <br>
Mitigation: Use minimal non-sensitive samples, avoid private or confidential text, and review generated output before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/gzh-copywriter) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [公众号趋势数据格式说明](references/gzh_trend_data_format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown article package with recommended titles, publish-ready body copy, core viewpoint, tags, differentiation notes when applicable, and viral-pattern source analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces roughly 1500 Chinese characters of WeChat article copy and may include summarized trend metrics from RedFox query results.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
