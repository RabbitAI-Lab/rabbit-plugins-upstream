## Description:

帮助内容运营人员查询抖音公开作品、评论和热榜数据，分析账号表现与选题趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

短视频运营、品牌和市场研究人员用它查找抖音公开内容、比较对标账号的作品互动，并分析评论与热点，辅助选题和运营决策。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords or links and the API token are sent to guaikei.com.

Mitigation: Use only when third-party data sharing is acceptable; keep the token private and avoid sensitive inputs.

Risk: Creator, post and comment results may remain in local logs.

Mitigation: Restrict access to saved results and delete logs when they are no longer needed.

Risk: Public creator and comment data can be used outside authorized purposes.

Mitigation: Analyze only authorized public data in accordance with Douyin terms and applicable privacy rules.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/why20261/skills/douyin-account-teardown)
- [Access and usage help](https://www.guaikei.com)
- [Command options](references/options.md)
- [Release notes](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Analysis guidance]

**Output Format:** [Markdown with command examples and summaries of structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator-post and comment results may be saved locally as JSON.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
