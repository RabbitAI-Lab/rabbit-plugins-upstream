## Description:

帮初中物理老师把讲题升级为系统化的解题教学，围绕审题、建模、过程分析、列式、求解反思、变式训练和班级解题档案形成可复用指导。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External teachers and education agents use this skill to turn junior-middle-school physics problem explanation into structured teaching guidance, model-selection prompts, variation practice, and class-level problem-solving records.

### Deployment Geography for Use:

Global, subject to local student-data, guardian-consent, and emergency-referral requirements before use outside mainland China.

## Known Risks and Mitigations:

Risk: Classroom records, student aliases, or writeback data could be stored or shared without the expected consent controls.

Mitigation: Use the skill only on platforms that enforce teacher confirmation, consent checks, aliasing, deletion/export controls, and sharing restrictions before records are stored or sent.

Risk: AI-generated or adapted physics items could contain incorrect calculations, unsuitable difficulty, or unsupported source use.

Mitigation: Label AI-generated questions, run the item-check workflow, require manual teacher verification before entry into repositories or assessments, and mark copyright status for each item.

Risk: Use outside mainland China may conflict with local student-data, guardian-consent, or emergency-referral requirements.

Mitigation: Review local legal requirements, replace region-specific help channels, and avoid presenting mainland-China emergency numbers as universal before deployment in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-problem-guide)
- [Five-step template](references/five-step-template.md)
- [Five-step worked examples](references/five-step-worked-examples.md)
- [Model selection](references/model-selection.md)
- [Physics variation training](references/variation-physics.md)
- [Multi-solution example](references/multi-solution-example.md)
- [Student solving profile template](references/student-solving-profile-template.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Platform conventions](shared/platform-conventions.md)
- [AI item check](shared/ai-item-check.md)
- [Shared vocabulary](shared/vocab.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown teaching guidance with optional structured classWorkspace proposals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required for stored records or writeback; AI-generated questions are labeled for manual checking.]

## Skill Version(s):

2.1.6 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
