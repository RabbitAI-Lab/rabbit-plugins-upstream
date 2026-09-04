## Description:

智能错题本 is a Chinese-language tutoring skill that records wrong answers across subjects, classifies each error by root cause, tracks repeated weak points, and prepares confirmed learning handoffs or reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language students and tutoring agents use this skill to capture wrong answers, identify the main error cause, maintain weak-point counts, and generate review reports or handoff records for related subject skills.

### Deployment Geography for Use:

Global, with local crisis and emergency resources configured for the learner's locale.

## Known Risks and Mitigations:

Risk: Long-term student profiles, reminders, parent-visible summaries, and cross-skill sharing can involve minors' educational data.

Mitigation: Confirm student or guardian consent for profiles, sharing, reminders, and parent-visible summaries before use.

Risk: Crisis referral resources may not match every deployment locale.

Mitigation: Configure and verify local crisis and emergency resources outside mainland China before deployment.

Risk: Root-cause analysis can be unreliable when the problem statement, image, or student process is incomplete.

Mitigation: Ask for confirmation, label insufficient evidence, and avoid writing unverified conclusions to long-term records.

Risk: Generated similar or practice questions may contain errors.

Mitigation: Self-solve and apply the item-check protocol before presenting generated exercises or storing them for reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [Error analysis framework](artifact/references/error-analysis-framework.md)
- [Shared vocabulary](artifact/shared/vocab.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Crisis exception protocol](artifact/shared/crisis-exception.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese-language conversational guidance, structured Markdown reports, and JSON handoff records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation before long-term record writeback or cross-skill sharing; full behavior depends on platform memory, OCR, and statistics support.]

## Skill Version(s):

2.1.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
