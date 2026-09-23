## Description:

初中数学分层进阶练习：在某个知识点已经会做的前提下，按 5 层难度定位当前练习层级，再一层一层往上练。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese middle-school learners and their supporting agents use this skill to place a math knowledge point on a five-level practice gradient, generate progressively harder exercises, record growth diary entries, and plan weekly retests with consent-aware profile and reminder handoffs.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: The skill can write student math profile data, share learning records across skills, surface parent-facing summaries, and enqueue reminders.

Mitigation: Confirm student or guardian consent before cross-skill sharing, profile writes, parent sharing, or reminder handoffs, and honor the documented view, correction, deletion, pause, sharing-control, and export controls.

Risk: The security guidance limits normal deployment to Mainland China Chinese K12 contexts because language, curriculum, privacy expectations, and crisis-contact guidance may not transfer directly.

Mitigation: Do not deploy outside the localized Chinese middle-school context until curriculum language, privacy handling, and emergency referral channels are adapted and reviewed.

Risk: Generated math exercises or gradient placements can be misleading if the agent emits flawed items or draws conclusions from too little evidence.

Mitigation: Apply the bundled item-check protocol before presenting generated questions, require at least two to three items per level for placement, and mark single-session results as preliminary.

Risk: A learner may disclose self-harm, abuse, bullying, severe despair, or another crisis signal during tutoring.

Mitigation: Stop the tutoring flow immediately and follow the bundled crisis exception and referral protocol, including localized emergency guidance and minimal factual logging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Gradient level reference](references/gradient-levels.md)
- [AI item check protocol](shared/ai-item-check.md)
- [Hint ladder](shared/hint-ladder.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [Platform conventions](shared/platform-conventions.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Conversational text and Markdown with optional structured JSON handoff payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include math practice questions, tier-placement feedback, growth diary entries, profile-writeback payloads, and reminder handoff proposals.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
