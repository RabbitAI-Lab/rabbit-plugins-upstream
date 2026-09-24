## Description:

Monitors restricted area intrusions, climbing on dining tables, and rummaging through trash cans, and issues real-time alerts, suitable for home pet monitoring scenarios. | 宠物禁区预警技能，监测禁止区域闯入、攀爬餐桌、翻垃圾桶行为并实时报警，适用于家庭宠物监控场景

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and pet owners use this skill to analyze home pet monitoring images or videos for restricted-area entry, table climbing, and trash-rummaging behavior, then receive structured warning reports and report links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or household monitoring media may be sent to a configured cloud service.

Mitigation: Use the skill only with videos or URLs that are appropriate for cloud processing, and avoid sensitive household footage unless privacy, retention, and access terms are clear.

Risk: Report history is tied to an automatically managed local or backend identity.

Mitigation: Review identity, token storage, and account-isolation behavior before deployment, especially on shared systems.

Risk: Cloud report history retrieval has limited user-facing privacy controls.

Mitigation: Restrict use to trusted environments and verify that users understand where report history is stored and retrieved.

## Reference(s):

- [API 接口文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-restricted-area-warning-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown or JSON structured pet restricted-area warning report, with optional saved output file and report link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or video URLs, supports basic, standard, and json detail levels, and can list cloud report history.]

## Skill Version(s):

1.0.15 (source: server release metadata; artifact frontmatter states 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
