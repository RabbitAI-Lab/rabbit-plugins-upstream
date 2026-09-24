## Description:

A Chinese K12 history essay coaching skill that guides middle and high school students through open-ended history argument questions by helping them extract their own claim from source material, choose supporting facts, organize reasoning, and check source-evidence alignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners in Chinese K12 history contexts use this skill to practice open-ended history essay questions. It supports claim extraction, evidence selection, argument organization, and self-checking while avoiding writing the student's claim or essay.

### Deployment Geography for Use:

China mainland by default; other regions require localized curriculum assumptions, consent handling, and crisis-referral channels before deployment.

## Known Risks and Mitigations:

Risk: The skill is designed for Chinese K12 history-learning contexts, so curriculum assumptions and crisis-referral channels may be unsuitable elsewhere.

Mitigation: Deploy it only in that context or localize curriculum references, consent handling, and crisis-referral channels before use.

Risk: The skill can update limited learning-profile fields and enqueue study reminders when authorized.

Mitigation: Enable profile updates and reminders only after learner and guardian consent settings are confirmed, and honor pause, export, deletion, and sharing controls.

Risk: The skill supports student-facing essay practice and could be misused to replace the learner's own reasoning.

Mitigation: Use it for guided questions, rubric-based self-checks, and feedback; require the student to write claims and final responses.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-history-essay-coach)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Essay rubric](artifact/references/essay-rubric.md)
- [History error dimension table](artifact/shared/history-error-dimension-table.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Learning profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, analysis, configuration]

**Output Format:** [Markdown or plain-text tutoring responses, with structured profile or reminder handoff fields only when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Consent-gated learning-profile updates and reminder handoffs; no shell commands.]

## Skill Version(s):

2.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
