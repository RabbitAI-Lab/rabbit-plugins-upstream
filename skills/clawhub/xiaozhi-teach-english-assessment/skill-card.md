## Description:

Helps Chinese-speaking K12 English teachers design four-skill assessments, create CSE-first and CEFR-referenced ability profiles, and draft teaching intervention guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External K12 English teachers in Mainland China use this skill to turn English tests into listening, speaking, reading, and writing assessments with ability profiles and follow-up teaching suggestions. It supports teacher-reviewed assessment design and optional class-workspace write-back rather than autonomous grading or ranking.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Student privacy or sensitive learning records could be exposed if real names or unnecessary personal details are entered.

Mitigation: Use student aliases and class numbers, keep reports de-identified, and only write back teacher-approved low-sensitivity facts.

Risk: Unreleased exam materials, answer keys, or scoring standards could be mishandled.

Mitigation: Do not enter unreleased unified exam content; use the skill for methods, frameworks, and self-authored practice materials instead.

Risk: AI-generated assessment items may contain errors or unsuitable difficulty.

Mitigation: Label AI-generated items, run the item self-check protocol, and require teacher verification before adding items to formal resources or tests.

Risk: Regional curriculum, privacy, or emergency-response assumptions may be wrong outside Mainland China.

Mitigation: Localize curriculum mappings, legal defaults, and crisis referral channels before use in other regions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-english-assessment)
- [CEFR/CSE can-do statements and level decision workflow](references/cefr-can-do-statements.md)
- [Four-skill English assessment rubric](references/four-skill-rubric.md)
- [English comprehensive assessment template](references/assessment-template.md)
- [CEFR four-skill descriptor quick reference](references/cefr-four-skill-descriptors.md)
- [Comprehensive assessment sample](references/comprehensive-assessment-sample.md)
- [Student ability profile template](references/student-ability-profile-template.md)
- [Teaching intervention suggestion sample](references/intervention-suggestion-sample.md)
- [English growth archive sample](references/english-growth-archive-sample.md)
- [AI item self-check protocol](shared/ai-item-check.md)
- [Class teaching workspace schema](shared/class-teaching-workspace.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions and downgrade paths](shared/platform-conventions.md)
- [Unified vocabulary](shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown text with structured tables, rubrics, templates, and optional JSON handoff examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are drafts for teacher review; write-back entries require teacher confirmation and consent.]

## Skill Version(s):

2.3.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
