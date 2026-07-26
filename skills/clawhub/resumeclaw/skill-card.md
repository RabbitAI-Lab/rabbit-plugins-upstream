## Description: <br>
Manage a ResumeClaw career agent that represents a user's professional experience to recruiters, including agent creation, inbox review, introduction decisions, agent search, profile review, notifications, and agent chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hherzai-crypto](https://clawhub.ai/user/hherzai-crypto) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and recruiters use this skill to manage ResumeClaw career agents from chat, including creating an agent from resume text, reviewing recruiter introductions, searching profiles, chatting with agents, and managing notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive career, account, resume, inbox, introduction, and notification data. <br>
Mitigation: Use it only with a ResumeClaw account and data the user is comfortable sending to resumeclaw.com, and upload only the intended resume text. <br>
Risk: The local login session persists at ~/.resumeclaw/session. <br>
Mitigation: On shared machines, remove ~/.resumeclaw/session after use if the user does not want the session to persist. <br>
Risk: The security review reports a search query and location encoding bug that can run unintended local code. <br>
Mitigation: Avoid free-form search queries or locations until the bug is fixed, and review search commands before execution. <br>


## Reference(s): <br>
- [ResumeClaw ClawHub listing](https://clawhub.ai/hherzai-crypto/skills/resumeclaw) <br>
- [ResumeClaw API Reference](references/api.md) <br>
- [ResumeClaw web dashboard](https://resumeclaw.com) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call resumeclaw.com, can read resume text, and store an authenticated session at ~/.resumeclaw/session.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
