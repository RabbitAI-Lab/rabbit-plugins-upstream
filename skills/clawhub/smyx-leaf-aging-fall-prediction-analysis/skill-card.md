## Description:

Analyzes houseplant leaf images or videos to report aging trends and estimate leaf-fall risk over the next 3–7 days.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Plant owners, horticultural teams, and gardening app developers use this skill to review leaf aging, anticipate possible shedding, and plan routine plant care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant photos, videos, or submitted URLs are processed by the Life Emergence cloud service, potentially exposing sensitive indoor imagery or private links.

Mitigation: Use only non-sensitive media and public URLs unless the publisher clearly documents data retention and deletion practices.

Risk: The skill silently creates or reuses an identity and stores service tokens locally, with limited user control over account linking.

Mitigation: Review identity storage and account-linking practices before installation; avoid using the skill until those practices meet your requirements.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or JSON analysis report, with Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes aging observations, estimated shedding risk, care suggestions, and report links; predictions are for plant-care guidance.]

## Skill Version(s):

1.0.17 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
