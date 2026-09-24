## Description:

A Chinese-language middle-school math coaching skill that helps learners convert word-problem text into equations through quantity identification, relationship phrasing, and algebraic translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 learners use this skill to practice modeling middle-school math word problems before equation solving. Tutors, guardians, or learning platforms can use it to guide hint-based coaching, worked-example escalation, and handoff once the equation has been formed.

### Deployment Geography for Use:

Global, with mainland China localization as the default; localize crisis-help channels and minor-data requirements before use outside mainland China.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese-language K12 math tutoring, especially mainland China curriculum contexts, so safety and curriculum assumptions may not transfer unchanged to other regions.

Mitigation: Before deployment outside mainland China, localize crisis-help channels, curriculum terminology, and minor-data consent requirements.

Risk: The skill may interact with learner profile, sharing, and guardian-visible summaries for minors.

Mitigation: Review profile, memory, sharing, and parent-consent controls before use; honor the artifact's pause, delete, export, and sharing-control commands.

Risk: The skill is scoped to translating word-problem text into equations and can mislead learners if used for full equation solving or unrelated subjects.

Mitigation: Keep coaching within quantity identification, relationship phrasing, and equation setup; hand off solving, geometry, pure algebra, and physics problems to the appropriate skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-word-problem-coach)
- [五大应用题题型建模框架与数量关系速查表](artifact/references/modeling-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown]

**Output Format:** [Markdown conversational tutoring guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Short Chinese-language coaching responses with hint-ladder constraints; no executable code.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
