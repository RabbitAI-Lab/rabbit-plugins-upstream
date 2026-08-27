## Description:

Evaluates interview and job-offer opportunities with six A-H dimension grades, an overall 1-5 score, action recommendations, interview-practice value, and risk notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[calmdowntr](https://clawhub.ai/user/calmdowntr)

### License/Terms of Use:

MIT-0

## Use Case:

Job seekers use this skill after receiving an interview invitation or offer to evaluate the opportunity against salary, company maturity, technical growth, work rhythm, stability, and location fit. It can also compare multiple opportunities and separate interview-practice value from whether the user should accept the job.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may save career preferences, salary floors, job status, and related profile details in a local user_profile.md file for future evaluations.

Mitigation: Review, edit, or delete the local user_profile.md file if those details should not persist or be reused.

Risk: Job-company assessments can be affected by incomplete user input or stale web-search results.

Mitigation: Use source snippets for key claims, mark unconfirmed information clearly, and ask focused follow-up questions instead of guessing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/calmdowntr/skills/job-screener-engine)
- [Scoring framework](references/scoring_framework.md)
- [Setup wizard](references/setup_wizard.md)
- [Information checklist](references/info_checklist.md)
- [User profile template](references/user_profile.TEMPLATE.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with scoring tables, source notes, and concise recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cited source snippets and up to three follow-up questions when job information is incomplete.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter and changelog report 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
