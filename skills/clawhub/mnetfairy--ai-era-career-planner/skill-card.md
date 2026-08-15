## Description:

AI Era Career Planner helps users assess interests, values, AI disruption risk, salary context, and learning paths to produce a personalized career planning report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mnetfairy](https://clawhub.ai/user/mnetfairy)

### License/Terms of Use:

MIT-0

## Use Case:

External users and career advisors use this skill for career planning, education-path selection, career transitions, and AI-era job-risk analysis. It guides a conversation, applies interest and values frameworks, and returns actionable career recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may ask for personal career details such as age, education, interests, city, and goals.

Mitigation: Collect only information needed for the requested planning task, avoid unnecessary sensitive details, and keep outputs in the conversation unless the user requests export or storage.

Risk: Optional integrations could send email, subscribe the user to updates, save long-term records, or use live job-search APIs.

Mitigation: Use integrations only after explicit user request and approval, and disclose what data will be sent, stored, or queried before taking action.

Risk: Insurance-industry recommendations include a featured referral list and phone numbers.

Mitigation: Present company information as optional reference material, disclose referral context, encourage independent credential checks, and do not contact companies on the user's behalf.

Risk: Career recommendations and AI replacement ratings are planning judgments and may be uncertain or time-sensitive.

Mitigation: Frame outputs as guidance rather than guarantees, state uncertainty where relevant, and encourage users to validate market conditions before making major career or education decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner)
- [Career assessment framework](references/assessment.md)
- [AI career impact reference](references/ai_career_impact.md)
- [Career anchor reference](references/career_anchor.md)
- [Salary data reference](references/salary_data.md)
- [Salary database](references/salary_database.json)
- [Job demand reference](references/job_demand.md)
- [Industry trends reference](references/industry_trends.md)
- [Education paths reference](references/education_paths.md)
- [Optional integrations reference](references/integrations.md)
- [Career planning tracker reference](references/tracker_system.md)
- [Insurance broker company data](references/insurance_broker_companies.json)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Conversational text or structured Markdown career planning report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May optionally export a Markdown report when the host environment permits it and the user explicitly requests it.]

## Skill Version(s):

2.2.296 (source: server release metadata; artifact frontmatter reports 2.2.250)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
