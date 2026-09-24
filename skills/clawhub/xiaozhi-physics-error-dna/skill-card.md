## Description:

Chinese-language physics error analysis skill for middle-school through first-year high-school learners that classifies mistakes across physics picture-building, concepts, formulas, process analysis, and math-tool use, then produces weak-point reports and consent-gated learning-profile updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and learning-support agents use this skill to analyze recurring physics mistakes, identify root causes, and generate weak-point reports or profile updates when consent allows. It is intended for Chinese K12 physics learning workflows, especially junior high and first-year high-school mechanics coverage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive student error and profile data may be shared more broadly than the core tutoring workflow requires.

Mitigation: Keep cross-skill sharing disabled unless needed, restrict handover recipients to documented recipients, and require explicit consent for parent-visible, emotion-related, and reminder outputs.

Risk: Consent expectations, curriculum assumptions, and crisis contacts are tailored to Chinese K12 physics contexts.

Mitigation: Localize curriculum scope, consent rules, and crisis referral contacts before deployment outside Mainland China Chinese K12 settings.

Risk: The skill may produce educational diagnoses about learners' weak points and physics anxiety.

Mitigation: Use the outputs as learning-support guidance, review age-sensitive outputs before sharing, and follow the bundled crisis protocol when self-harm, bullying, severe distress, or safety concerns appear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-error-dna)
- [Physics error dimension table](artifact/references/physics-error-dimension-table.md)
- [Physics concept confusion map](artifact/references/physics-concept-confusion-map.md)
- [Physics math tools checklist](artifact/references/physics-math-tools-checklist.md)
- [Physics diagram guide](artifact/shared/physics-diagram-guide.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese Markdown responses with JSON-compatible profile and handover records when the host platform supports them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce consent-gated physics error profiles, weak-point reports, reminder handoff records, and crisis-referral guidance.]

## Skill Version(s):

2.3.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
