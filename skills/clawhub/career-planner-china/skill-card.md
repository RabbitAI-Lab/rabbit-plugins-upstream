## Description:

A Chinese-language AI-era career-planning assistant that guides users through career assessments and provides personalized recommendations, education paths, and analysis of AI's impact on work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students and professionals use the skill to explore career options, education paths, and career changes in China. It gathers a user profile and offers assessment-informed recommendations with salary, job-demand, and AI-impact context.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan reports possible write-scope mismatches, including persistent-memory writes beyond the tracker scope.

Mitigation: Review write paths and require an explicit user request and path validation before exporting reports or writing tracking records.

Risk: Inspection was partial: 25 of 26 components were fully inspected, and static parsing of the salary database was limited, so some content remains unverified.

Mitigation: Review salary data and verify figures against current sources before relying on them in career recommendations.

## Reference(s):

- [Career Planner China on ClawHub](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [Career assessment methods](references/assessment.md)
- [AI career impact analysis](references/ai_career_impact.md)
- [Salary data](references/salary_data.md)
- [Job demand trends](references/job_demand.md)
- [Education paths](references/education_paths.md)
- [Insurance company recommendations](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown]

**Output Format:** [Conversational guidance and a structured Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized to the user's profile; file export is optional and user-requested.]

## Skill Version(s):

2.3.8 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
