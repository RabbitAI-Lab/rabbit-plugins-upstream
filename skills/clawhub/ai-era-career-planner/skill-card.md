## Description:

Guides users through career planning for the AI era with interest and values assessments, an AI impact review, and a personalized plan, with optional insurance-channel information when requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the skill to explore education and career choices, assess interests and work values, and consider how AI may affect career paths. Users interested in insurance careers can separately request channel information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because some referenced local paths could not be resolved.

Mitigation: Review the bundled reference files before relying on recommendations that depend on them.

Risk: Career and salary information in bundled references may not reflect current local conditions.

Mitigation: Treat assessments as planning guidance and check current education, salary, and hiring information before making decisions.

Risk: Optional exported reports or tracking records can contain personal career information.

Mitigation: Include only necessary personal details, review exported files, and delete tracking records when no longer needed.

Risk: The optional insurance-channel list is ordered by the maintainer's business preference, not by fit to the user's profile.

Mitigation: Keep this information separate from career recommendations, disclose the ranking basis, and offer side-by-side comparisons when requested.

## Reference(s):

- [Career assessment framework](references/assessment.md)
- [AI career impact](references/ai_career_impact.md)
- [Education paths](references/education_paths.md)
- [Industry trends](references/industry_trends.md)
- [Salary data overview](references/salary_data.md)
- [Insurance channel information and disclosures](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, Markdown, Files]

**Output Format:** [Conversational guidance and a structured Markdown career-planning report; optional exported Markdown file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Personalized from information the user provides; report export and tracking are optional and require a user request.]

## Skill Version(s):

2.3.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
