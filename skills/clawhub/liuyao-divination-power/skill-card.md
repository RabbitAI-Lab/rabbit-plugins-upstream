## Description:

专业六爻纳甲筮法排盘与解卦，自动起卦排盘并按十步流程分析用神、旺衰、动变、伏神、世应、六神兽、应期和 HTML 报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanding1998](https://clawhub.ai/user/seanding1998)

### License/Terms of Use:

个人免费·商业授权

## Use Case:

External users and divination practitioners use this skill to turn a question or manually supplied hexagram into a traceable Liuyao analysis workflow with generated case files and an HTML report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs bundled Python scripts and may install an unpinned third-party Python package.

Mitigation: Run it only in a trusted agent environment; review commands before execution and pin or preinstall dependencies from trusted sources.

Risk: The skill creates persistent local case folders containing detailed user questions and generated reports.

Mitigation: Avoid highly sensitive questions and delete generated case folders when the reading no longer needs to be retained.

Risk: Untrusted text may pass through command construction and generated HTML paths.

Mitigation: Treat user-supplied text as untrusted, prefer argument-array command execution, and escape all user-controlled fields before sharing HTML output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seanding1998/skills/liuyao-divination-power)
- [Rule index](references/rule-index.md)
- [HTML report guide](references/html-report-guide.md)
- [解卦详解](references/jie-gua-xiang-jie.md)
- [六亲六神兽类象](references/liuqin-liushen-leixiang.md)
- [地支关系](references/di-zhi-relations.md)
- [动变法则](references/dong-bian-fa-ze.md)
- [应期法则](references/yingqi-faze.md)
- [五行生克](references/wuxing-shengke.md)
- [六十四卦](references/64-gua.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML files, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with local JSON and HTML report artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates persistent local case folders for each reading and may invoke bundled Python scripts.]

## Skill Version(s):

2.0.1 (source: SKILL.md frontmatter, CHANGELOG, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
