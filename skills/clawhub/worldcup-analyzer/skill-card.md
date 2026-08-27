## Description:

Predict English Premier League football match outcomes first, keep World Cup national-team support for compatibility, include schedule/result context, answer in the user's language, and keep output as statistical reference only, never betting advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[datatrevor](https://clawhub.ai/user/datatrevor)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate statistical football matchup analysis, with EPL matchups as the primary flow and World Cup national-team matchups retained for compatibility. It provides modeled outcome, expected goal difference, schedule or result context, quota guidance, and non-betting compliance language.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Football matchup queries and any configured SOCCER_API_KEY are sent to the configured prediction service.

Mitigation: Install only if comfortable with that data flow, keep WORLDCUP_API_BASE at the documented production host unless deliberately testing another service, and avoid sharing sensitive matchup context.

Risk: Dependency versions are lower-bounded rather than pinned.

Mitigation: Review and tighten dependency versions before production deployment.

Risk: Users may try to use statistical predictions as betting advice.

Mitigation: Keep the mandatory statistical-reference disclaimer, refuse betting picks, stake sizing, bookmaker odds, and under-18 use, and redirect users to modeled outcome and expected goal difference only.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/datatrevor/skills/worldcup-analyzer)
- [Football Match Analyzer API Reference](artifact/references/api.md)
- [Schedule And Result Reference](artifact/references/schedule.md)
- [Extended Compliance Notes](artifact/references/compliance.md)
- [Canonical Team Names](artifact/references/team_names.md)
- [Prediction Service](https://www.jiajielitong.com)
- [2026 FIFA World Cup Schedule Reference](https://en.wikipedia.org/wiki/2026_FIFA_World_Cup)
- [2026 FIFA World Cup Baidu Baike Fallback](https://baike.baidu.com/en/item/2026%20FIFA%20World%20Cup/1497370#9)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with modeled outcome, expected goal difference, schedule or result context, quota notes, and a mandatory statistical-reference disclaimer.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should match the user's language, avoid betting advice, and treat low expected-goal-difference margins as near-draws.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter, evidence release metadata, README changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
