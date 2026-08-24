## Description:

清华校园技能包（统一入口）。涵盖网络学堂、课表、成绩、培养方案、选课、第二成绩单、邮箱、文献、图书馆、座位预约、研读间、校内通知和水木搜索等校园事务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT-0

## Use Case:

Students and campus users use this skill to let an agent initialize credentials, route natural-language requests, and automate everyday Tsinghua campus services such as coursework, schedules, grades, library actions, notices, literature search, and email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to handle sensitive campus and email credentials.

Mitigation: Install only when comfortable with local credential handling, keep credentials in the configured secure storage, and avoid exposing passwords or tokens in prompts, files, or command arguments.

Risk: The skill can automate account-changing actions such as homework submission, email sending, marking mail as read, seat booking, or cancellation.

Mitigation: Review confirmations and results carefully before allowing the agent to complete actions under the user identity.

Risk: Exported transcripts, cookies, browser profiles, and credential fallback files may contain sensitive local data.

Mitigation: Treat generated local artifacts and session state as sensitive data and restrict access to the local machine and workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tomuiv/skills/tsinghua-campus)
- [Publisher profile](https://clawhub.ai/user/tomuiv)
- [Project repository declared in skill documentation](https://github.com/TOMUIV/tsinghua-campus-skill)
- [README](artifact/README.md)
- [Credential configuration guide](artifact/campus/CREDS.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with JSON-producing command workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests across campus service subskills and may produce local files such as downloaded course materials or exported PDFs.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
