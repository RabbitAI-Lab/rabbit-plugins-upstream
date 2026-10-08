## Description:

Helps Chinese K–12 students maintain a consent-based learning profile, including progress, learning preferences, and optional emotional-learning observations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students and their guardians use this skill to create, inspect, correct, export, or delete a long-term learning profile for personalized educational support. Optional emotional observations and sharing require separate consent.

### Deployment Geography for Use:

Chinese K–12 settings; other regions require localization

## Known Risks and Mitigations:

Risk: Long-term educational and emotional records about minors could be exposed to another student or shared without consent.

Mitigation: Verify per-student isolation, default-off consent, guardian consent where required, and field-level limits on cross-skill sharing and teacher writeback before enabling persistent profiles.

Risk: Students may be unable to control sensitive records after collection.

Mitigation: Confirm that the host platform reliably supports viewing, correcting, exporting, and deleting each student's profile.

Risk: Crisis referrals and educational guidance may not fit a student's region.

Mitigation: Use only in the intended Chinese K–12 setting or localize it first, including region-appropriate crisis referral information.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-dna)
- [Learning-profile schema guide](artifact/schemas/README.md)
- [Learning-profile template](artifact/references/dna-template.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Conversational profile summaries and structured learning-profile records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile access and updates are consent-gated; students may request export or deletion.]

## Skill Version(s):

2.11.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
