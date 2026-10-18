## Description:

帮助中国大陆中小学教师梳理知识图谱、识别重难点并制定间隔回看与交叉练习的复习排期。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中小学教师，根据教学进度与班级共性薄弱知识点制定单元、期中、期末或考前复习计划；具体作业和试卷交由其他技能处理。

### Deployment Geography for Use:

中国大陆；其他地区使用前需本地化课程、未成年人数据要求及危机求助渠道

## Known Risks and Mitigations:

Risk: 课程口径、同意要求或危机求助资源不适用于部署地区。

Mitigation: 用于中国大陆中文 K12 教师场景；在其他地区使用前核对课程、同意要求并替换当地危机求助资源。

Risk: 复习计划可能暴露学生个人信息或未经教师同意保存。

Mitigation: 仅读取制定排期所需的班级字段；写入前征得教师确认，使用化名并排除个人分数和排名。

Risk: 将严重心理危机当作一般考前紧张处理。

Mitigation: 出现危机信号时停止复习规划，按当地转介流程联系可信赖的成年人及专业资源。

## Reference(s):

- [ClawHub 技能发布页](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [复习策略与排期](references/review-strategy.md)
- [知识图谱范例](references/knowledge-map-example.md)
- [重难点清单模板](references/key-points-checklist-template.md)
- [复习活动样例库](references/review-activity-library.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown 复习排期表、知识图谱与重难点清单]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [仅制定复习计划；保存计划须经教师确认，不包含学生真实姓名、个人分数或排名。]

## Skill Version(s):

2.11.2 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
