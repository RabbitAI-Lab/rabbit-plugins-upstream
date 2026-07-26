## Description: <br>
AI-era-career-planner helps agents guide Chinese-language career planning conversations with staged intake, interest and values assessment, AI job-impact analysis, salary and demand references, and personalized action plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and career guidance agents use this skill to plan education choices, career entry, or career transitions in the AI era. The skill supports structured intake, assessment, career recommendations, AI-resilience guidance, and concrete next-step planning. <br>

### Deployment Geography for Use: <br>
Global, with China-focused salary and insurance company reference data. <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask for personal career-context information. <br>
Mitigation: Collect only information the user chooses to provide and avoid saving profiles unless the user explicitly requests a saved record. <br>
Risk: Salary references and insurance company recommendations may be stale, incomplete, or mistaken for endorsement. <br>
Mitigation: Treat salary and company data as reference material, keep insurance recommendations disclosed as informational, and ask users to verify details before acting. <br>
Risk: Optional email, subscription, live-search, or saved-record actions can affect user data outside the conversation. <br>
Mitigation: Only use optional integrations when the current environment permits them and the user has clearly approved the specific action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/ai-era-career-planner) <br>
- [AI career impact reference](references/ai_career_impact.md) <br>
- [Career assessment framework](references/assessment.md) <br>
- [Career anchor reference](references/career_anchor.md) <br>
- [Education paths](references/education_paths.md) <br>
- [Job demand trends](references/job_demand.md) <br>
- [Industry trends](references/industry_trends.md) <br>
- [Salary data](references/salary_data.md) <br>
- [Insurance broker company reference](references/insurance_broker_companies.json) <br>
- [Optional integrations reference](references/integrations.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Files] <br>
**Output Format:** [Markdown career planning report and conversational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally generate a Markdown report file when the host environment allows it and the user explicitly requests export.] <br>

## Skill Version(s): <br>
2.2.240 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
