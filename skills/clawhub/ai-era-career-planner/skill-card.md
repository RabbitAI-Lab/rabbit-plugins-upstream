## Description:

An AI-era career-planning skill that gathers a user's background and interests, assesses career values and AI-related job impacts, and creates a personalized career plan, with an optional, separately disclosed insurance-channel directory when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People choosing a field, planning a career change, or assessing how AI may affect their work use it to build a personalized plan based on their interests, values, education paths, job demand, and salary references. People who explicitly ask about insurance work can also request its separately ranked channel directory.

### Deployment Geography for Use:

Global, with many market references focused on China

## Known Risks and Mitigations:

Risk: Career, AI impact, salary, and job-demand guidance relies on references that may not reflect current local conditions.

Mitigation: Treat recommendations as planning input and compare them with current local information before making career or education decisions.

Risk: The optional insurance directory's priority order is a maintainer business preference, not a ranking based on a user's fit.

Mitigation: Ask for side-by-side channel comparisons and verify a provider's credentials and coverage before contacting it.

Risk: Optional career tracking retains user-provided details for up to 90 days when explicitly requested.

Mitigation: Review what is saved, request deletion when it is no longer needed, and use tracking only when it suits your needs.

Risk: The security assessment was benign with medium confidence, and some referenced paths could not be matched to bundled files.

Mitigation: Review the career-planning features and optional tracking or report export against your needs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment methods](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchors](references/career_anchor.md)
- [Education paths](references/education_paths.md)
- [Job demand trends](references/job_demand.md)
- [Industry trends](references/industry_trends.md)
- [Salary reference](references/salary_data.md)
- [Insurance channel directory and disclosures](references/insurance_broker_companies.json)
- [Insurance provider information](https://www.axa.com.hk/zh/who-we-are)
- [National financial regulator](https://www.nfra.gov.cn/)
- [Optional career tracking guidance](references/tracker_system.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Analysis, Markdown]

**Output Format:** [Conversational guidance and structured Markdown career-planning reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided details; report export and career tracking are optional and require an explicit request.]

## Skill Version(s):

2.3.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
