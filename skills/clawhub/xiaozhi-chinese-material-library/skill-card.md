## Description:

A Chinese-language writing-materials library that saves and tags students' excerpts, retrieves them by topic, and suggests how to use them in writing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and educators use this skill to collect and tag Chinese writing excerpts, retrieve relevant material for essays, and review usage or monthly summaries. A separate writing coach leads the essay-writing workflow.

### Deployment Geography for Use:

Global; localize emergency referrals and review guardian-consent settings outside Mainland China.

## Known Risks and Mitigations:

Risk: Students' saved writing materials or usage records could be shared without appropriate consent, particularly for minors.

Mitigation: Check student or guardian consent and platform memory settings before saving or sharing; honor deletion, no-memory and no-sharing requests, and share only consented usage counts.

Risk: Unverified quotations or missing sources could mislead students or encourage inaccurate citations.

Mitigation: Record sources for high-school material, label uncertain attributions for verification, and ask for the original text rather than reconstructing quotations.

Risk: Cross-session material and monthly totals may be unavailable when the platform lacks memory or history capabilities.

Mitigation: Explain session-only storage and offer a text export; do not present session totals as historical monthly counts.

Risk: A student may disclose harm or immediate danger during a learning conversation.

Mitigation: Stop the materials workflow, direct the student to a trusted adult and location-appropriate help, and do not give Mainland China emergency numbers without confirming the student's location.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-chinese-material-library)
- [Platform capabilities and privacy controls](shared/platform-conventions.md)
- [Student profile and consent schema](shared/dna-profile.schema.json)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tagged excerpts with source labels and suggested uses; on-request usage summaries and text exports.]

## Skill Version(s):

2.9.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
