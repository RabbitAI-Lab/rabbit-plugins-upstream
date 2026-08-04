## Description: <br>
Career Planner China helps users plan education, career direction, and career transitions in the AI era by collecting profile details, assessing interests and values, evaluating AI job-impact risk, and producing a personalized career plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and career advisors use this skill to explore China-focused career options, education paths, AI-era job risks, salary expectations, and short-term action plans. It is designed for students, graduates, and workers considering career choices or transitions. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal education, career, preference, and location details to tailor advice. <br>
Mitigation: Provide only details needed for the planning task and avoid retaining, exporting, emailing, or subscribing the user to follow-up services without an explicit request. <br>
Risk: Optional report export, memory tracking, email sending, subscriptions, or live job-data lookup could externalize user career information. <br>
Mitigation: Use bundled offline data by default and require clear user approval before any export, persistence, outbound message, subscription, or live lookup. <br>
Risk: Insurance-company recommendations could affect career or employment decisions. <br>
Mitigation: Treat insurance-company options as informational and compare them independently before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [Publisher profile](https://clawhub.ai/user/mnetfairy) <br>
- [Career assessment framework](references/assessment.md) <br>
- [MBTI quick reference](references/mbti.md) <br>
- [Career anchor reference](references/career_anchor.md) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Salary reference](references/salary_data.md) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Education paths](references/education_paths.md) <br>
- [2026 emerging careers](references/emerging_industries/2026_careers.md) <br>
- [Insurance broker company data](references/insurance_broker_companies.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational text or structured Markdown career planning report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional Markdown report export when explicitly requested and allowed.] <br>

## Skill Version(s): <br>
2.2.275 (source: server release evidence; artifact frontmatter lists 2.2.255) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
