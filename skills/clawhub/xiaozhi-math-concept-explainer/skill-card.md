## Description:

Helps Chinese junior-high students understand math concepts through everyday analogies, visual reasoning, and step-by-step decomposition, then checks understanding with restatement, examples, or transfer questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students in Chinese junior-high math use this skill when they are stuck on the meaning of a concept rather than on one specific problem. It supports concept explanations, spatial reasoning for geometry, and brief verification prompts after explanation.

### Deployment Geography for Use:

China mainland Chinese-language K12 context unless curriculum, emergency contacts, and minor-consent rules are localized for another region.

## Known Risks and Mitigations:

Risk: The skill is designed around Chinese-language K12 curriculum assumptions, emergency contacts, and minor-consent rules.

Mitigation: Use it in the intended Chinese-language K12 context, or localize curriculum scope, emergency channels, and consent rules before deployment.

Risk: Long-term memory, parent visibility, or cross-skill sharing could expose student learning records if enabled without consent review.

Mitigation: Review profile, deletion/export, parent-sharing, and cross-skill-sharing controls before enabling persistent memory or shared reports.

Risk: Generated verification questions or examples may be unsuitable if they exceed the intended grade band or are not checked.

Mitigation: Apply the included AI item self-check process and keep generated math questions within the declared junior-high scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-concept-explainer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Junior-high math analogy bank](artifact/references/analogy-bank.md)
- [Platform conventions and localization guidance](artifact/shared/platform-conventions.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Concise Chinese tutoring dialogue in plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for short concept explanations with follow-up checks; the skill states a single-message budget of about 120 Chinese characters and up to three follow-up turns.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
