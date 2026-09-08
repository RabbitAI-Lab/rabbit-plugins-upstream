## Description:

Career Planner China helps users plan career directions for the AI era in Chinese education and work contexts by collecting user background, assessing interests and values, rating AI career impact, and producing personalized career planning reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill to conduct AI-era career planning conversations for Chinese education and work contexts, including interest and personality assessment, salary and demand lookup, and personalized next-step planning.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Insurance-interested users may be steered toward a maintainer-chosen priority company and phone contact.

Mitigation: Review the insurance recommendation behavior before deployment, keep the recommendation optional, require explicit user consent before showing contact details, and present alternatives with the skill's disclaimer.

Risk: The optional report export helper can overwrite an existing same-named writable file.

Mitigation: Run report export only in a controlled directory and confirm the output location before executing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mnetfairy/skills/career-planner-china)
- [AI career impact reference](references/ai_career_impact.md)
- [Career assessment framework](references/assessment.md)
- [MBTI career personality reference](references/mbti.md)
- [Career anchor reference](references/career_anchor.md)
- [Salary data reference](references/salary_data.md)
- [Detailed salary database](references/salary_database.json)
- [Job demand trends](references/job_demand.md)
- [Industry trend analysis](references/industry_trends.md)
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md)
- [Insurance broker company data](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown career planning report with structured recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output is conversational; optional report export can create a Markdown file when explicitly requested.]

## Skill Version(s):

2.2.403 (source: server release metadata; artifact frontmatter reports 2.2.260)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
