## Description:

根据行业名称和时间窗口生成六节 A 股行业景气报告，提供带日期、口径和来源锚的冷热证据并标示覆盖缺口；不提供个股推荐或择时建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT-0

## Use Case:

面向行业研究人员和投资尽调团队，用于行业研究开题、会前准备及尽调报告中的行业章节；整理有来源依据的行业数据证据、代表公司和覆盖缺口。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional connectivity check may expose CUE_API_KEY to an unverified destination, and its default-send behavior is described inaccurately.

Mitigation: Do not enable API access until the destination is verified; before using --post, require verified HTTPS destinations and redirect protections. For an offline connectivity check, use --catalog-file without --post.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huhoo/skills/cue-sector-overview)
- [Section skeleton](artifact/references/section-skeleton.md)
- [Policy timeline](artifact/references/policy-timeline.md)

## Skill Output:

**Output Type(s):** [Markdown report, Source index, Review checklist]

**Output Format:** [Markdown 六节行业报告，含表格、来源锚与复核清单]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [标注数据日期、比较口径和覆盖缺口；不提供个股评级或择时建议。]

## Skill Version(s):

0.1.29 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
