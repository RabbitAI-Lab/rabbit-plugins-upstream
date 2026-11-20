## Description:

A career-planning skill that helps users assess their interests and values, understand how AI may affect career options, and build a personalized plan.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

People in China seeking help with career choices, education paths, or a work transition can use the skill to explore their profile and receive a structured plan informed by local career, salary, and industry references. Insurance-channel information is available only when the user explicitly asks about that field.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence, and some local references could not be resolved.

Mitigation: Treat career and salary estimates as planning input, confirm relevant current information, and discuss uncertainty with the user.

Risk: The optional insurance-channel ordering reflects the maintainer's business preference rather than a personalized assessment.

Mitigation: Disclose the basis for the ordering, offer side-by-side comparisons, and provide the module only when the user explicitly asks about insurance careers or channels.

## Reference(s):

- [Career assessment framework](references/assessment.md)
- [AI and career impact](references/ai_career_impact.md)
- [Career anchors](references/career_anchor.md)
- [Education paths](references/education_paths.md)
- [Industry trends](references/industry_trends.md)
- [Job demand trends](references/job_demand.md)
- [Salary data](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Insurance channel information and disclosures](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational guidance and a structured Markdown career-planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from user-provided information; may include assessments, career options, AI-impact notes, and next steps. Insurance-channel details are optional and user-triggered.]

## Skill Version(s):

2.3.19 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
