## Description: <br>
Career Planner China helps Chinese-speaking users plan education and career moves in the AI era by collecting profile details, applying career-interest and values assessments, estimating AI impact, and producing personalized career planning reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Chinese-speaking students, job seekers, and career switchers use this skill to explore majors, career paths, AI-era occupational risk, salary expectations, industry trends, and concrete next steps. It is designed for conversational career guidance and structured personalized reports, not as a substitute for professional financial, legal, or employment advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal education, career, interests, values, and location information to produce advice. <br>
Mitigation: Share only information needed for the planning task and avoid unnecessary sensitive identifiers. <br>
Risk: Optional email sending, subscriptions, memory tracking, real-time search, and report export can externalize or persist user data. <br>
Mitigation: Enable these features only after an explicit user request and after confirming the host environment allows the action. <br>
Risk: Salary data and insurance-company recommendations may be incomplete or out of date. <br>
Mitigation: Independently verify salary ranges, job demand, and insurance-company options before making career or financial decisions. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [Career planning conversation flow](references/flow_engine.md) <br>
- [Career assessment framework](references/assessment.md) <br>
- [MBTI career personality reference](references/mbti.md) <br>
- [Career anchor reference](references/career_anchor.md) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Salary data reference](references/salary_data.md) <br>
- [Detailed salary database](references/salary_database.json) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Education paths](references/education_paths.md) <br>
- [2026 emerging careers in China](references/emerging_industries/2026_careers.md) <br>
- [Insurance broker company data](references/insurance_broker_companies.json) <br>
- [Optional integrations](references/integrations.md) <br>
- [Career tracking system](references/tracker_system.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Conversational guidance and structured Markdown career planning reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional Markdown report export only when the user requests it and the host allows file generation.] <br>

## Skill Version(s): <br>
2.2.253 (source: server release metadata; artifact frontmatter lists 2.2.194) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
