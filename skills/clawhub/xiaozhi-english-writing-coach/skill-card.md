## Description:

英语写作进化教练 helps Chinese-language K12 learners improve English writing through sentence-level grammar, vocabulary, and logic feedback, guided revision prompts, scenario practice, and consent-gated writing profiles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, parents, teachers, and education operators use this skill as a Chinese-language English writing coach for paragraph and essay feedback, sentence upgrade practice, and progress reporting. It is intended for normal learning support, not active exams, crisis counseling, or unconsented student profiling.

### Deployment Geography for Use:

Global, with localization required for emergency resources, curriculum assumptions, and minor-consent rules before student use outside Mainland China.

## Known Risks and Mitigations:

Risk: The skill is designed for K12 learners, so student use may require adult supervision, consent, and local minor-data handling rules.

Mitigation: Require parent or teacher presence for younger learners, enable long-term writing profiles only after consent, and localize consent controls before deployment.

Risk: Crisis signals such as self-harm, bullying, serious despair, or family safety concerns are outside the learning-coach scope.

Mitigation: Stop tutoring flow, avoid judgment, explain the AI boundary, contact a trusted adult, and route the learner to local emergency or crisis resources.

Risk: Emergency contacts, curriculum assumptions, and consent expectations may not match regions outside Mainland China.

Mitigation: Replace emergency resources, school-stage assumptions, and consent language with locally appropriate guidance before serving those users.

Risk: The coach could over-assist by effectively writing an assignment for the learner or helping during an active exam.

Mitigation: Use hint ladders and example patterns instead of writing the learner's paragraph or essay, and pause support until after any active exam or test.

## Reference(s):

- [Skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-english-writing-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Vocabulary upgrade reference](references/vocabulary-upgrade.md)
- [English error dimension table](shared/english-error-dimension-table.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Crisis exception](shared/crisis-exception.md)
- [Hint ladder](shared/hint-ladder.md)
- [Platform conventions](shared/platform-conventions.md)
- [Unified vocabulary](shared/vocab.md)
- [Grade bands](shared/grade-bands.md)
- [AI item check protocol](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Chinese-language coaching dialogue and Markdown feedback, with occasional structured profile or handoff snippets when consent allows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focuses on 2-3 priority issues per writing sample; does not write full arguments, paragraphs, or essays for the learner.]

## Skill Version(s):

2.3.0 (source: server release evidence, target metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
