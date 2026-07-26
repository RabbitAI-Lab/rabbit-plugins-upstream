## Description: <br>
Analyzes fixed-camera videos to estimate adolescents' head posture and handheld-device use, summarize screen-looking time, and produce behavior reminders and reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, guardians, educators, and developers use this skill to analyze home, study-room, or classroom camera videos for screen-looking posture patterns and generate structured reports with gentle intervention suggestions. It is intended for visual behavior statistics, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can upload sensitive videos of minors to a remote service. <br>
Mitigation: Use only with guardian and child consent, confirm the destination service, and require documented retention, deletion, authorization, and access-control practices before deployment. <br>
Risk: Cloud report history and account identity reuse can expose reports beyond the intended user. <br>
Mitigation: Restrict history lookups to authorized users, verify report access controls, and avoid broad automatic history retrieval unless the user has a clear need. <br>
Risk: Visual classification may mistake normal reading, writing, or online classes for problematic screen use. <br>
Mitigation: Review outputs before acting, keep reminders gentle, and do not treat the report as a diagnosis or disciplinary basis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-teen-screen-addiction-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include posture statistics, screen-time summaries, reminder text, report links, and history-report tables.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
