## Description:

Guides students through weekly interest exploration to distinguish surface likes from interests that remain compelling when the student encounters difficulty, with explicit consent before durable tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners and education-support agents use this skill to run age-appropriate weekly interest exploration, capture consented interestDNA signals, and produce student-facing reflections or parent summaries only under the required sharing consent. It is intended for interest discovery, not subject tutoring, career planning, admissions advice, or psychological diagnosis.

### Deployment Geography for Use:

China mainland by default; localize crisis channels, school-stage assumptions, and minor-consent rules before use in other regions.

## Known Risks and Mitigations:

Risk: The release is a child-focused durable interest tracker, and the security evidence says its bundled schema permits broader profile and reminder changes than the skill needs.

Mitigation: Constrain operation to interestDNA-only profile writes, require profileEnabled and interestTrackingConsent, require guardian consent where applicable, and limit reminders to explicit interest-exploration follow-ups.

Risk: The security evidence classifies the release as suspicious unless platform controls enforce the intended consent and write limits.

Mitigation: Review platform enforcement before installation and scan the package so profile writes, sharing, and reminders cannot exceed the skill's stated scope.

Risk: The skill includes crisis-support routing that is written for China mainland and can be inappropriate if reused unchanged elsewhere.

Mitigation: Localize emergency and youth-support channels before deployment outside China mainland, and ask for the user's country or region before giving region-specific crisis numbers.

Risk: Interest conclusions can mislead students if based on too little observation or treated as career or admissions advice.

Mitigation: Use the skill's confidence labels, avoid writing insufficient samples to long-term records, and keep outputs framed as interest-exploration signals rather than academic, career, or admissions recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration template](artifact/references/interest-exploration-template.md)
- [Grade bands](artifact/shared/grade-bands.md)
- [Vocabulary and consent fields](artifact/shared/vocab.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [LearningDNA profile schema](artifact/shared/dna-profile.schema.json)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Chinese conversational guidance with structured Markdown templates and JSON-compatible profile or handover fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces consent-gated interest records, reflection summaries, parent-facing factual summaries when allowed, and profile or reminder handoff fields.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
