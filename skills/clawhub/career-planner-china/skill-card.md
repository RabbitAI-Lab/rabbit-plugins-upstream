## Description: <br>
Career Planner China is a Chinese-language career planning skill that collects user context, applies Holland, MBTI, career-anchor, and values signals, assesses AI-era career impact, and produces personalized career planning reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mnetfairy](https://clawhub.ai/user/mnetfairy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, students, and career changers use this skill for AI-era career planning in China, including major selection, role transitions, industry fit, salary context, and action plans. The skill is intended to provide structured career guidance, not guaranteed employment, recruiting, legal, financial, or mental-health advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Career recommendations may be misunderstood as deterministic predictions or professional guarantees. <br>
Mitigation: Present recommendations as planning guidance, include uncertainty and disclaimers, and encourage users to compare options against their own circumstances and current market evidence. <br>
Risk: Optional email, subscription, live lookup, export, or recruiting-data actions can expose personal career information outside the local conversation. <br>
Mitigation: Use the skill's default offline posture and perform these actions only when the user explicitly requests them and the host grants permission. <br>
Risk: Optional memory or tracking features can persist user profile and career-plan details. <br>
Mitigation: Do not create profiles, write memory files, or schedule follow-up contact unless the user explicitly asks for persistence and the host environment supports it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mnetfairy/skills/career-planner-china) <br>
- [AI career impact reference](artifact/references/ai_career_impact.md) <br>
- [Assessment reference](artifact/references/assessment.md) <br>
- [Career anchor reference](artifact/references/career_anchor.md) <br>
- [Salary data reference](artifact/references/salary_data.md) <br>
- [Emerging industries 2026 reference](artifact/references/emerging_industries/2026_careers.md) <br>
- [Integration controls reference](artifact/references/integrations.md) <br>
- [Tracking controls reference](artifact/references/tracker_system.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Conversational Chinese text and structured Markdown career-planning reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include user profile summaries, career fit ratings, AI impact labels, salary ranges, action plans, and optional Markdown report files when explicitly requested.] <br>

## Skill Version(s): <br>
2.2.273 (source: server release metadata; artifact frontmatter reports 2.2.255) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
