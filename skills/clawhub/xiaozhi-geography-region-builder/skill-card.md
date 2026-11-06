## Description:

陪学生通过定位、归纳特征、比较和联系四步认识世界、中国及家乡的区域，并学习高中区域发展、资源环境与国家安全相关内容。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

初中和高中学生可用此技能练习描述区域的位置与特征、比较两个区域并说明区域联系；高中学生还可学习课程范围内的城乡空间、区域发展及资源环境与国家安全内容。

### Deployment Geography for Use:

中国大陆；其他地区需本地化危机求助渠道与相关指导。

## Known Risks and Mitigations:

Risk: Persistent student records, sharing, or reminders depend on host platform and companion skills whose storage and deletion behavior is not included in this package.

Mitigation: Keep the default session-only mode; before enabling records, sharing, or reminders, check the host platform's and companion skills' storage and deletion controls.

Risk: The learning content targets mainland Chinese schools, and crisis-support contacts may not apply in other regions.

Mitigation: Localize crisis guidance and support contacts for the deployment region; if the user's region is unknown, ask before naming local contacts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-geography-region-builder)
- [Region cognition guide](artifact/references/region-cognition-guide.md)
- [High school required geography topics](artifact/references/region-hs-required.md)
- [High school regional development](artifact/references/region-development-hs.md)
- [Resources, environment, and national security](artifact/references/resources-environment-security-hs.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese tutoring dialogue, regional summaries, comparison tables, and practice guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-only by default; learning records require consent and item-by-item confirmation.]

## Skill Version(s):

2.12.6 (source: evidence.json release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
