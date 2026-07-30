## Description: <br>
AI-Era Career Planner is a career-planning assistant that gathers user career context, applies interest and values assessments, evaluates AI-era job impact, and produces personalized career planning guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill for AI-era career planning, major selection, career transition advice, and job direction recommendations. It produces a structured plan with profile assessment, career options, AI impact ratings, salary and demand context, learning paths, and immediate next actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal career, education, interests, goals, and location details to produce recommendations. <br>
Mitigation: Collect only information needed for the requested planning task, avoid unnecessary sensitive detail, and do not persist a profile unless the user explicitly asks. <br>
Risk: The insurance-company recommendation path could be perceived as an endorsement or sales push. <br>
Mitigation: Keep the disclosure and disclaimer visible, present company information neutrally, and do not contact companies or initiate sales actions for the user. <br>
Risk: Optional email, subscription, live lookup, memory, or tracking integrations could externalize or retain user data. <br>
Mitigation: Use integrations only after explicit user authorization and confirm the destination, action, and data to be shared before proceeding. <br>
Risk: Career planning recommendations, salary references, and job demand trends are decision-support guidance and may be incomplete or outdated. <br>
Mitigation: Frame outputs as probabilistic guidance, include uncertainty, and encourage users to verify salary, hiring, and education details before making major decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner) <br>
- [Career assessment framework](references/assessment.md) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Salary data reference](references/salary_data.md) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Optional integrations reference](references/integrations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown career planning report with structured sections; optional Markdown file export when explicitly requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline-first; optional integrations only with explicit user authorization.] <br>

## Skill Version(s): <br>
2.2.251 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
