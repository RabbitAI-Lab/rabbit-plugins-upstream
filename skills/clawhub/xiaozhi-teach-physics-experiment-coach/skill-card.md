## Description:

Helps middle-school physics teachers organize experiment instruction across goals, design, implementation, data processing, conclusions, lab reports, safety levels, grouping, and equipment planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External middle-school physics teachers use this skill to plan, run, and review physics experiment lessons, including experiment type selection, variable control, safety handling, student grouping, data tables, conclusions, and lab-report feedback. The skill is designed for teacher-mediated classroom use rather than autonomous experiment execution or direct grading.

### Deployment Geography for Use:

China mainland by default; non-China deployments should localize curriculum alignment, privacy-law assumptions, and emergency referral wording.

## Known Risks and Mitigations:

Risk: The skill may handle minor student classroom records, parent-facing outputs, and cross-skill sharing settings.

Mitigation: Before installation, confirm the platform enforces teacher confirmation, consent checks, privacy controls, sharing opt-outs, export, correction, and deletion flows.

Risk: The skill is designed around China mainland K12 curriculum, privacy assumptions, and emergency referral wording.

Mitigation: For non-China deployments, localize curriculum references, applicable privacy-law assumptions, consent requirements, and emergency help wording before use.

Risk: Physics experiments can involve safety-sensitive classroom activity.

Mitigation: Require each experiment to carry a safetyLevel; high-risk experiments should be demonstration-only or replaced with video or simulation, with teacher supervision for medium-risk work.

Risk: AI-generated experiment plans or assessment items could contain inaccurate calculations, unsafe assumptions, or unsuitable grade-level content.

Mitigation: Mark AI-generated items for human verification and require teacher review before classroom use, resource-bank storage, or student-facing distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-physics-experiment-coach)
- [Skill definition](artifact/SKILL.md)
- [Initial physics experiment types](artifact/references/experiment-types.md)
- [Experiment design sample](artifact/references/experiment-design-sample.md)
- [Data record samples](artifact/references/data-record-samples.md)
- [Data processing rubric](artifact/references/data-processing-rubric.md)
- [Conclusion sample](artifact/references/conclusion-sample.md)
- [Lab report template](artifact/references/lab-report-template.md)
- [Lab report sample](artifact/references/lab-report-sample.md)
- [Student lab profile template](artifact/references/student-lab-profile-template.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Shared vocabulary](artifact/shared/vocab.md)
- [AI item check](artifact/shared/ai-item-check.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese Markdown guidance with tables, checklists, templates, and structured class-workspace fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is expected for saved records, AI-generated items, parent-facing outputs, and safety-sensitive classroom decisions.]

## Skill Version(s):

2.1.6 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
