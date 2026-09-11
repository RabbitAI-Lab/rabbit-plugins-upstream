## Description:

清华校园技能包（统一入口）帮助 Agent 处理网络学堂、课表、成绩、培养方案、选课、第二成绩单、邮箱、文献、图书馆座位、校内通知、搜索和地图等校园事务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT-0

## Use Case:

Tsinghua University community members use this skill through an Agent to initialize local credentials and automate routine campus workflows such as checking coursework, schedules, grades, library availability, notices, literature, email, and campus map queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and credential/session handling create high-impact trust risk.

Mitigation: Install only after trusting the publisher and browser download mirrors; prefer an isolated user profile and clear local sessions or cookies when finished.

Risk: Campus credentials, mail credentials, and external API keys may expose sensitive personal or institutional data.

Mitigation: Provide only required credentials, avoid storing optional mail credentials unless needed, and review the external Scopus client before using Scopus keys.

Risk: Reservations, cancellations, email sends, and assignment submissions are real account actions.

Mitigation: Require explicit user confirmation before write actions and present consequences such as cancellation limits, check-in requirements, or irreversible submissions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tomuiv/skills/tsinghua-campus)
- [ClawHub publisher profile](https://clawhub.ai/user/tomuiv)
- [README](artifact/README.md)
- [Credential guide](artifact/campus/CREDS.md)
- [Course reverse notes](artifact/docs/course-reverse-notes.md)
- [Library reverse notes](artifact/docs/library-reverse-notes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON script results, configuration instructions, and generated or downloaded files when a workflow requires them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Handles sensitive campus data and can trigger real account actions such as assignment submissions, email sends, reservations, and cancellations.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
