## Description:

清华校园技能包（统一入口）。涵盖网络学堂/课表/成绩/培养方案/选课/第二成绩单/邮箱/文献/图书馆/座位预约/研读间/校内通知/水木搜索等校园事务。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomuiv](https://clawhub.ai/user/tomuiv)

### License/Terms of Use:

MIT-0

## Use Case:

Tsinghua University students and campus users use this skill to let an agent initialize credentials and assist with campus workflows such as coursework, timetables, grades, library reservations, campus notices, literature search, mail, and local map queries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Tsinghua CAS credentials, campus records, reusable login sessions, and optional mailbox access.

Mitigation: Use it only in an isolated or dedicated local environment, avoid syncing runtime data, and proceed only when the user accepts this account and data access.

Risk: The skill can perform real-world write actions such as sending email, submitting homework, making bookings, and cancelling reservations.

Mitigation: Require explicit user confirmation before any email, homework submission, booking, cancellation, or comparable write action.

Risk: The security evidence flags review needs around mirror-based browser installation, browser no-sandbox launch, local session and mail credential storage, and autonomous code repair.

Mitigation: Review these behaviors before deployment and require explicit confirmation before any local code change.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tomuiv/skills/tsinghua-campus)
- [ClawHub publisher profile](https://clawhub.ai/user/tomuiv)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text summaries with JSON-backed command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include campus data summaries, credential setup guidance, confirmation prompts for write actions, and local configuration steps.]

## Skill Version(s):

1.0.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
