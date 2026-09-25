## Description:

指导开发者编写和检查面向中国 K12 学习场景的 SKILL，涵盖角色、规则、记忆、输出及安全与隐私边界。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

SKILL 开发者以及具备编程或提示词基础的高中生，可用它起草或排查学习类 SKILL 的结构、行为规则、授权边界和交接方式；它不提供学科辅导或练习题。

### Deployment Geography for Use:

中国大陆（现有模板与求助渠道按此地区编写；其他地区须先本地化）

## Known Risks and Mitigations:

Risk: Chinese K12 templates may give unsuitable curriculum, consent, or emergency guidance outside mainland China.

Mitigation: Localize curriculum, minor-consent rules, templates, and local emergency contacts before using elsewhere.

Risk: The referenced SECURITY_BASELINE.md is absent from the release package.

Mitigation: Obtain and review the applicable security and privacy baseline before relying on its requirements.

Risk: Generated learning skills could retain minors' data or share sensitive information without adequate consent.

Mitigation: Review generated skills for explicit consent, guardian authorization where needed, minimum data sharing, and deletion controls before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-creator)
- [SKILL 提示词模板库](references/skill-templates-library.md)
- [统一词表与阈值](shared/vocab.md)
- [平台能力与隐私控制入口](shared/platform-conventions.md)
- [危机例外与转介](shared/crisis-exception.md)
- [档案字段定义](shared/dna-profile.schema.json)
- [交接协议字段定义](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown SKILL.md drafts, templates, and review guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory text only; does not access student records or execute code.]

## Skill Version(s):

2.4.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
