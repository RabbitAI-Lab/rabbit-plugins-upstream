## Description:

小红书搜索雷达通过关键词检索公开笔记，并查询笔记详情、评论、博主作品及粉丝等互动数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

小红书创作者、品牌运营和市场研究人员可用它检索公开笔记、评论、博主作品及互动数据，为选题、竞品观察、KOL筛选和舆情梳理收集资料。结果用于个人或团队内部分析，不替代用户判断。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search keywords and supplied links are sent to guaikei.com.

Mitigation: Use a dedicated GUAIKEI_API_TOKEN and avoid submitting sensitive keywords or links.

Risk: Successful queries and results are saved locally by default.

Mitigation: Set XHS_GUAIKEI_DISABLE_LOG=1 before running if local log files are not wanted.

## Reference(s):

- [参数与调用说明](references/options.md)
- [常见问题排查](references/troubleshooting.md)
- [使用说明](readme.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON response envelope containing public note search results, note details, comments, or creator profile and engagement data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public content; requires GUAIKEI_API_TOKEN. Successful queries and results are saved locally by default; XHS_GUAIKEI_DISABLE_LOG=1 disables local logging.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
