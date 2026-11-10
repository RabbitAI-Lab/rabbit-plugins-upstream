## Description:

该技能查询小红书公开笔记、评论和博主数据，并以 JSON 返回，供选题、竞品和舆情分析使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

小红书创作者、运营人员、品牌和经纪团队可用它查询公开笔记、评论及博主作品和互动数据，为选题研究、竞品观察、KOL筛选和评论归纳提供结构化资料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send search terms and supplied Xiaohongshu links to Guaikei; provider-side data handling was not verified.

Mitigation: Use only public-data queries and avoid including sensitive information in search terms or links.

Risk: API calls may consume paid token quota, with lower per-query limits for some plans.

Mitigation: Check the applicable plan limits and requested result count before running a query.

Risk: Results may be saved in local temporary files by default.

Mitigation: Set XHS_GUAIKEI_DISABLE_LOG=1 to prevent new result files and remove existing logs when no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/um-why/skills/xiaohongshu-tool)
- [Guaikei Service](https://www.guaikei.com/)
- [参数与调用说明](artifact/references/options.md)
- [常见问题排查](artifact/references/troubleshooting.md)
- [更新日志](artifact/references/changelog.md)
- [GitHub Issues](https://github.com/um-why/xiaohongshu-openclaw-skill/issues)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [JSON envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Structured public post, comment, and creator data for follow-on analysis; read-only platform access.]

## Skill Version(s):

1.2.1 (source: SKILL.md frontmatter, changelog, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
