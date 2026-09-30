## Description:

在明确授权下管理中国中小学生的长期学习档案，支持查看、更正、导出和删除，并记录经确认的成长里程碑。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to manage a consent-based learning profile for personalized tutoring, including strengths, challenges and progress. Educators may contribute limited updates only with the required permissions and student confirmation.

### Deployment Geography for Use:

China (Chinese K–12 context)

## Known Risks and Mitigations:

Risk: Sensitive student profiles could be exposed across users or shared without permission.

Mitigation: Deploy only where per-student isolation, consent state, export and deletion, and field-level cross-skill controls can be enforced.

Risk: Minor-consent and crisis-referral practices may not fit deployments outside the documented setting.

Mitigation: Keep use within the Chinese K–12 context unless local crisis resources and minor-consent rules have been adapted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning profile template](references/dna-template.md)
- [Growth milestones](references/growth-milestones.md)
- [Crisis referral protocol](references/crisis-referral-protocol.md)
- [Learning profile schema and consent model](schemas/README.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Chinese-language guidance, profile summaries and structured learning-profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and updates require the applicable consent and student confirmation; exports are provided as text.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
