## Description:

Provides a Chinese middle-school math gradient trainer that locates a student's current practice level for a known topic, then generates progressively harder exercises, hints, training reflections, and review checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and tutoring agents use this skill for Chinese middle-school math practice after a student can already solve the basic topic. It assesses a five-level practice gradient, generates targeted exercises and hints, summarizes growth, and prepares consent-gated learning-log or reminder handoffs.

### Deployment Geography for Use:

China mainland by default; other regions require localization of emergency resources, curriculum alignment, and minor-data consent rules before student-facing use.

## Known Risks and Mitigations:

Risk: The security review says the active instructions omit required crisis routing for minors.

Mitigation: Require crisis routing to appear before exercise, fallback, and data-display flows, and route self-harm, abuse, bullying, severe despair, or family-safety signals to the bundled crisis protocol before continuing math practice.

Risk: The security review says the profile writeback schema is broader than the skill's stated purpose.

Mitigation: Enforce writeback only to the intended math gradient and training-log fields, and require affirmative cross-skill sharing consent before any handoff.

Risk: Generated math items can be invalid, ambiguous, or outside the declared middle-school scope.

Mitigation: Apply the bundled AI item self-check before presenting generated exercises: self-solve, confirm a valid solution, check condition sufficiency, keep numbers grade-appropriate, and stay within the declared grade band.

Risk: Default emergency contacts, curriculum assumptions, and minor-data rules are tailored to China mainland deployment.

Mitigation: Localize emergency resources, curriculum alignment, and consent requirements before using the skill with students in other regions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-gradient-trainer)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Gradient level reference](artifact/references/gradient-levels.md)
- [AI item self-check protocol](artifact/shared/ai-item-check.md)
- [Hint ladder](artifact/shared/hint-ladder.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Conversational Chinese text, Markdown summaries, and JSON handover payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces middle-school math exercises, stepwise hints, growth-diary summaries, consent-gated training-log writebacks, and reminder enqueue requests.]

## Skill Version(s):

2.1.10 (source: evidence.release.version and artifact/SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
