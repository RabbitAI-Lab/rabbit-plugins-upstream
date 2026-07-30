## Description: <br>
Provides Chinese-language AI-era career planning guidance by collecting user background, assessing career interests and values, evaluating AI impact on career paths, and producing a personalized career planning report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Chinese-speaking students and workers use this skill to explore majors, job options, career transitions, AI-era replacement risk, salary and demand signals, and concrete next steps. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for career goals, education background, work preferences, and other personal planning information. <br>
Mitigation: Collect only information needed for the current planning conversation and avoid storing, emailing, or subscribing the user unless they explicitly request it. <br>
Risk: Salary data, job-demand trends, and insurance-company recommendations may become outdated or may not match a user's location or situation. <br>
Mitigation: Treat these outputs as planning references and independently verify current salary ranges, hiring demand, and company details before acting on them. <br>
Risk: Optional report export, memory, email, subscription, and live-data integrations could create external side effects. <br>
Mitigation: Enable optional integrations only when the host environment allows them and the user has clearly authorized that action for the specific conversation. <br>


## Reference(s): <br>
- [AI Career Impact Reference](references/ai_career_impact.md) <br>
- [Career Assessment Framework](references/assessment.md) <br>
- [Career Anchor Reference](references/career_anchor.md) <br>
- [Education Paths](references/education_paths.md) <br>
- [Conversation Flow Engine](references/flow_engine.md) <br>
- [Industry Trends](references/industry_trends.md) <br>
- [Job Demand Trends](references/job_demand.md) <br>
- [Salary Data](references/salary_data.md) <br>
- [Salary Database](references/salary_database.json) <br>
- [2026 Emerging Careers China](references/emerging_industries/2026_careers.md) <br>
- [Insurance Broker Company Data](references/insurance_broker_companies.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational text and structured Markdown career-planning reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include optional Markdown report content when explicitly requested; scripts and integrations are not required by default.] <br>

## Skill Version(s): <br>
2.2.256 (source: server release metadata; artifact SKILL.md frontmatter reports 2.2.255) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
