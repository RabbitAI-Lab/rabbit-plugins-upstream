## Description:

Chinese-language K12 chemistry notation coach for element symbols, valence, chemical formulas, equation writing, and balancing from middle-school foundations through early high-school required chemistry.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External learners, teachers, and parents use this skill to practice and diagnose chemistry notation errors, including formula writing, equation balancing, reaction conditions, symbol meanings, and early high-school ion/electron-transfer notation.

### Deployment Geography for Use:

Mainland China curriculum context; localize curriculum, consent rules, and crisis-referral guidance before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside the intended simplified-Chinese mainland-China K12 chemistry context can misalign curriculum assumptions, consent handling, or crisis-referral guidance.

Mitigation: Install for the intended context, or localize curriculum scope, consent rules, and crisis-referral instructions before deployment.

Risk: Learner-profile or reminder features can affect minors' educational records or follow-up expectations.

Mitigation: Review learner-profile and reminder settings before enabling them, and require explicit consent for profile writes, cross-skill sharing, and reminders.

Risk: Generated chemistry practice items or notation feedback can be incorrect if not checked.

Mitigation: Use the bundled chemistry notation rules and AI item-check protocol for validation, and require human review for high-stakes or classroom-resource use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-chemistry-notation-coach)
- [Chemistry Notation Rules](references/chemistry-notation-rules.md)
- [Chemistry Error Dimension Table](shared/chemistry-error-dimension-table.md)
- [AI Item Check Protocol](shared/ai-item-check.md)
- [Learning DNA Profile Schema](shared/dna-profile.schema.json)
- [Handover Protocol Schema](shared/handover-protocol.schema.json)
- [Crisis Exception Protocol](shared/crisis-exception.md)
- [Crisis Referral Protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Conversational Markdown/text guidance with optional structured learner-profile and handoff data when consent is present.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose profile updates or reminders only after explicit consent; otherwise operates within the current conversation.]

## Skill Version(s):

2.3.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
