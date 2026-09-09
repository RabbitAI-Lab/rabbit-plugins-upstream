## Description:

Career Planner China helps users plan careers in the AI era with China-focused interest assessment, values analysis, AI impact ratings, salary context, and personalized action plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to collect a career profile, evaluate career fit, assess AI substitution risk, compare China-market salary and demand signals, and produce a structured career planning report. It is also used for optional industry-specific guidance, including insurance career onboarding recommendations when relevant.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance company recommendations may appear neutral while using a maintainer-selected priority order.

Mitigation: Disclose that ordering is maintainer-selected, compare multiple verified companies, and avoid presenting the ordering as an objective ranking.

Risk: The optional report export script can write files even though the skill declares no default write behavior.

Mitigation: Run report export only after explicit user request, choose a private destination, and confirm the output path before writing.

Risk: Career reports may contain personal profile details, preferences, and planning constraints.

Mitigation: Keep reports in a private directory, avoid unnecessary persistence, and do not send or store user profile details unless the user explicitly asks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI career impact reference](artifact/references/ai_career_impact.md)
- [Career assessment framework](artifact/references/assessment.md)
- [China salary database](artifact/references/salary_database.json)
- [2026 emerging careers reference](artifact/references/emerging_industries/2026_careers.md)
- [Insurance broker company dataset](artifact/references/insurance_broker_companies.json)
- [National Financial Regulatory Administration public query portal](https://www.nfra.gov.cn/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Files]

**Output Format:** [Markdown career planning report with structured recommendations and optional exported Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include career assessment summaries, AI risk labels, salary ranges, industry guidance, action plans, and optional private report export when explicitly requested by the user.]

## Skill Version(s):

2.2.405 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
