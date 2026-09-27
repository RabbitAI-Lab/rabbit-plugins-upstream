## Description:

A Chinese-language physics coach that guides middle-school and first-year high-school students through diagrams, modeling, calculation, and checking for a specific problem.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students in middle school through the first year of high school use this coach to work through a specific physics problem with step-by-step prompts, diagrams, and checks rather than receiving an immediate answer.

### Deployment Geography for Use:

Mainland China (localize curriculum, crisis contacts, and minor-consent rules for other regions)

## Known Risks and Mitigations:

Risk: A minor's learning profile, wrong answers, or reminders may be shared without their intended consent.

Mitigation: Verify platform enforcement of separate consent gates for profile access, each wrong-answer handoff, and reminders; keep the default session-only.

Risk: Curriculum assumptions and crisis contacts may not fit students outside Mainland China.

Mitigation: Localize the curriculum, crisis contacts, and minor-consent requirements before deploying elsewhere.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach)
- [Four-step problem-solving guide](artifact/references/physics-4step-statemachine.md)
- [Physics diagram guide](artifact/references/physics-diagram-guide.md)
- [Socratic questioning guide](artifact/references/physics-socrates-guide.md)
- [First-year high-school worked examples](artifact/references/physics-hs1-worked-examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational Markdown with step-by-step questions and worked explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional profile-based guidance and wrong-answer or reminder handoffs require separate consent.]

## Skill Version(s):

2.7.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
