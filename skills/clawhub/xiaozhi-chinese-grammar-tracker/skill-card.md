## Description:

A Simplified Chinese grammar coach that helps students identify six common sentence-error types and, with consent, track recurring errors and progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to diagnose and practice correcting Chinese sentence errors. With consent, it can maintain a recurring-error profile and provide progress summaries and writing-time prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Learner error records or reminders may be retained or shared without effective consent controls.

Mitigation: Before enabling persistence, verify the host enforces consent, deletion, pause, cross-skill and guardian-sharing restrictions, and reminder opt-in.

Risk: Grammar assessments and progress claims may be inaccurate when the host lacks memory or cross-session statistics.

Mitigation: Review uncertain classifications and limit progress reporting to available session data rather than inventing history.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-grammar-tracker)
- [Grammar error library](artifact/references/grammar-error-library.md)
- [High-school sentence guidance](artifact/references/chinese-hs-sentence.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Markdown]

**Output Format:** [Conversational Chinese text and optional Markdown progress reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional consent-controlled grammar-error profile and reminder handoffs; without persistence or cross-session statistics, report only current-session results.]

## Skill Version(s):

2.11.1 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
