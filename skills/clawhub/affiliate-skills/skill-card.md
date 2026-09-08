## Description:

Research and evaluate affiliate programs to find the best ones to promote.

This skill is ready for commercial/non-commercial use.

## Publisher:

[affitor](https://clawhub.ai/user/affitor)

### License/Terms of Use:

MIT-0

## Use Case:

Affiliate marketers and content creators use this skill to discover, compare, and score affiliate programs for a niche, audience, or promotion platform. It helps users evaluate commission terms, cookie windows, content potential, market demand, competition, and trust signals before choosing programs to promote.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Affiliate program data and terms can change after the skill retrieves them.

Mitigation: Verify commission rates, cookie windows, payout rules, and current program terms before acting on recommendations.

Risk: The skill may activate on broad monetization or niche-selection prompts and steer the conversation toward affiliate-program recommendations.

Mitigation: Confirm that the user wants affiliate-program research before narrowing recommendations to affiliate offers.

Risk: Public web or API data used for scoring can be stale or incomplete.

Mitigation: Prefer structured openaffiliate.dev API data, cite external search queries used for scoring, and flag program data older than six months.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/affitor/skills/affiliate-skills)
- [openaffiliate.dev](https://openaffiliate.dev)
- [openaffiliate.dev Data Access](artifact/references/openaffiliate-api.md)
- [Platform-Specific Affiliate Rules](artifact/references/platform-rules.md)
- [Program Scoring Framework](artifact/references/scoring-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown tables with JSON-compatible recommendation fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes ranked affiliate programs, a top pick, a runner-up, scoring rationale, and next-step guidance.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
