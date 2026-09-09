## Description:

英语综合测评设计：帮英语老师把一张卷子变成听说读写四维的能力测评与画像。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese K12 English teachers use this skill to design four-skill English assessments, summarize learner ability profiles, and plan teaching interventions from assessment evidence. It is intended for mainland China K12 settings unless localized for other regions.

### Deployment Geography for Use:

Mainland China; localize legal, crisis, and student-data guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill can support persistent class records and student-profile writeback in a K12 context.

Mitigation: Confirm teacher authorization and required consent before enabling persistence, use student aliases instead of real names, and honor data control requests for viewing, correction, deletion, export, pausing memory, and sharing limits.

Risk: The skill contains mainland China K12 assumptions, including assessment standards and crisis or legal guidance.

Mitigation: Use it where those assumptions fit, and localize standards, crisis referral paths, and legal guidance before non-mainland deployment.

Risk: AI-generated assessment items may contain errors or be unsuitable for direct use.

Mitigation: Require teacher review and verification before adding AI-generated items to a resource bank or exam blueprint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [Assessment template](references/assessment-template.md)
- [Four-skill rubric](references/four-skill-rubric.md)
- [Student ability profile template](references/student-ability-profile-template.md)
- [CEFR four-skill descriptors](references/cefr-four-skill-descriptors.md)
- [CEFR can-do statements](references/cefr-can-do-statements.md)
- [Teaching intervention sample](references/intervention-suggestion-sample.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance and structured assessment templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference class assessment records and student-profile writeback when consent and platform capabilities are available.]

## Skill Version(s):

2.1.12 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
