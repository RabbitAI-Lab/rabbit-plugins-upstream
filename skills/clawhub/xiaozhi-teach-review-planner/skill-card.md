## Description:

Helps Chinese K12 teachers turn review from reteaching into a paced plan with knowledge maps, priority topics, spaced recall, interleaved practice, review activities, and pre-exam state support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers use this skill to build unit, midterm, final, and pre-exam review plans that prioritize shared weak points, schedule spaced recall, and separate easily confused concepts. It produces planning guidance rather than full assignments or exam papers.

### Deployment Geography for Use:

Global, with Mainland China localization as the documented default for curriculum, emergency contacts, and minor-data consent assumptions.

## Known Risks and Mitigations:

Risk: The skill is written for Mainland China Chinese K12 review-planning workflows, so emergency contacts, curriculum mappings, and minor-data consent assumptions may be wrong elsewhere.

Mitigation: Localize emergency contacts, curriculum alignment, and consent rules before using the skill outside Mainland China.

Risk: Review plans may persist learner-related data if platform gates are not enforced.

Mitigation: Require teacher confirmation before writing reviewPlans and enforce documented reminder limits before enabling notifications.

Risk: Generated practice examples or variant questions could contain mistakes.

Mitigation: Apply the artifact's AI item-check process and mark generated items for human checking before adding them to a resource bank or exam paper.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-review-planner)
- [Publisher Profile](https://clawhub.ai/user/qizhitang)
- [Review Strategy](references/review-strategy.md)
- [Key Points Checklist Template](references/key-points-checklist-template.md)
- [Knowledge Map Example](references/knowledge-map-example.md)
- [Review Activity Library](references/review-activity-library.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown planning guidance with schedules, checklists, tables, and text templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose reviewPlans entries only after teacher confirmation; generated items require human checking before reuse.]

## Skill Version(s):

2.1.12 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
