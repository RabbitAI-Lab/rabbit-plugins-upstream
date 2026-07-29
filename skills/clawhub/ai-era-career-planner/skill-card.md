## Description: <br>
AI-era career planning skill that gathers career context, assesses interests and values, evaluates AI disruption risk, uses salary and demand references, and produces a personalized career plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and employees use this skill for career planning, major selection, career transition advice, and AI-era role selection. The skill produces structured recommendations with career fit, AI impact, salary context, learning paths, and next actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal education, career, city, and preference details to generate advice. <br>
Mitigation: Ask only for details needed for the career plan, avoid unnecessary sensitive data, and do not persist profile information unless the user explicitly requests it. <br>
Risk: Salary data and insurance-company listings are advisory and may be outdated or incomplete. <br>
Mitigation: Present these references as starting points, encourage independent verification, and avoid treating listed companies or salary ranges as guarantees. <br>
Risk: Optional report export, email sending, subscriptions, memory storage, or live web data can create external actions or persistence. <br>
Mitigation: Perform those actions only after explicit user authorization and confirm the destination, scope, and data to be shared or stored. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner) <br>
- [Assessment framework](references/assessment.md) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Salary data overview](references/salary_data.md) <br>
- [Salary database](references/salary_database.json) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Education paths](references/education_paths.md) <br>
- [Insurance broker company list](references/insurance_broker_companies.json) <br>
- [Optional integrations](references/integrations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown career planning report with structured recommendations and optional Markdown file export] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include salary ranges, AI impact ratings, learning paths, insurance-company information when relevant, and short action plans.] <br>

## Skill Version(s): <br>
2.2.248 (source: server release metadata; artifact frontmatter lists 2.2.190) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
