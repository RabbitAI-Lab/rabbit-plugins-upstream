## Description:

Helps biology and geography teachers plan junior-secondary academic-level exam and senior-secondary qualification exam review around local exam requirements and classroom needs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Biology and geography teachers in mainland China use this skill to map local exam requirements to curriculum topics, identify class-level gaps, plan safe practical preparation, and schedule review before the exam. Teachers review the proposed schedule before it is saved or shared.

### Deployment Geography for Use:

Mainland China; other regions require local curriculum and crisis-support guidance.

## Known Risks and Mitigations:

Risk: Incorrect review scope if local exam rules are missing or assumed from another region.

Mitigation: Use the current local exam notice supplied by the teacher; flag unknown requirements for confirmation and localize guidance outside mainland China.

Risk: Exposure of confidential exam material or identifiable student performance data.

Mitigation: Do not provide unreleased exam papers or real student names and scores; use class-level gaps and pseudonyms instead.

Risk: An inaccurate plan could be saved or used without teacher review.

Mitigation: Have the teacher review the generated plan and explicitly approve any workspace write.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-bio-geo-review-planner)
- [Biology and geography exam review guide](artifact/references/bio-geo-exam-review.md)
- [Senior-secondary biology exam review guide](artifact/references/biology-hs-exam-review.md)
- [Senior-secondary geography exam review guide](artifact/references/geography-hs-exam-review.md)
- [Laboratory safety guidance](artifact/shared/lab-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown topic map and dated review plan; optional structured review-plan entry after teacher confirmation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags missing local exam requirements for teacher confirmation; does not promise exam results.]

## Skill Version(s):

2.11.1 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
