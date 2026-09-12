## Description:

通过公众号文章数据自动提取交易体系、市场判断、表达风格、内容深度、互动特征、热点图谱和人设基因，生成结构化的投资博主七维 DNA 风格画像。

This skill is for research and development only.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

External users, investors, content creators, and researchers use this skill to collect WeChat public-account articles and produce a seven-dimensional investment blogger style profile for comparison, research, and style-reference workflows. Generated investment-style analysis is framed as AI style simulation and not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically install a dependency during environment checks.

Mitigation: Review the package installation behavior before use and run the skill in an isolated environment.

Risk: Fetched article content and generated profiles are stored under output/.

Mitigation: Delete generated output files when they are no longer needed and treat fetched article text as untrusted evidence.

Risk: User-provided account and author names influence generated file paths.

Mitigation: Use simple safe characters for account and author names, and add path containment checks before broader deployment.

Risk: Providing a RedFox key on the command line can expose credentials through shell history or process listings.

Mitigation: Prefer environment-variable configuration for REDFOX_API_KEY and avoid the --api-key argument.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/investor-distiller)
- [Publisher profile](https://clawhub.ai/user/yuanyi-github)
- [蒸馏维度规范](references/蒸馏维度规范.md)
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON profile/statistics files, with shell command examples and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes fetched article data, statistics, profile JSON, style-profile Markdown, and validation reports under output/.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
