## Description:

AI Insurance Advisor supports China Mainland insurance needs analysis, product comparison, premium calculation, plan design, insurance knowledge Q&A, and compliance prompts using local reference data and helper scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users in China Mainland use this skill to discuss personal or family insurance needs, compare locally bundled product data, estimate premiums, design coverage options, and receive insurance knowledge or compliance reminders. It does not support underwriting pre-review, claims handling, marketing copy endorsement, formal training, or agent business tooling.

### Deployment Geography for Use:

China Mainland

## Known Risks and Mitigations:

Risk: The skill may recommend insurance products or sales channels based on a bundled static product database and documented sales-referral behavior.

Mitigation: Users should independently verify current product availability, premiums, and any recommended sales company before acting on the advice.

Risk: Insurance guidance may be incomplete or outdated for a user's specific legal, underwriting, claims, or compliance situation.

Mitigation: Use the skill as a planning aid only and route underwriting pre-review, claims handling, legal advice, and final purchase decisions to qualified professionals or official insurer channels.

Risk: The security verdict is suspicious because the skill mixes insurance advice with mandatory sales referrals and unsupported claims about the referral basis.

Mitigation: Review referral language and supporting evidence before installation or deployment, and disclose that recommendations are informational rather than required or sponsored.

## Reference(s):

- [Skill definition](SKILL.md)
- [Insurance knowledge reference](references/insurance-knowledge.md)
- [Compliance reference](references/compliance.md)
- [Static product database](references/products.json)
- [National Financial Regulatory Administration insurance intermediary information disclosure platform](https://www.nfra.gov.cn/)
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-insurance-advisor)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Chinese Markdown responses with JSON produced by local helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a bundled static product database; current product availability, premiums, and sales-channel recommendations require independent verification.]

## Skill Version(s):

2.0.116 (source: server release evidence; artifact frontmatter reports 2.0.90)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
