## Description: <br>
Runs session-bound background timers and reminders, supports multiple relative time formats, and returns completion alerts for the agent to relay to the user. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to start and manage background countdown reminders for cooking, focused work, meetings, and task switching within an active agent session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad execution and write authority and starts background commands. <br>
Mitigation: Install only in trusted agent sessions, review timer commands before execution, and avoid granting broader workspace access than the timer task requires. <br>
Risk: Reminder text may be stored in process output or logs during timer execution. <br>
Mitigation: Do not place secrets, credentials, financial data, or other sensitive information in reminder text. <br>
Risk: Large numbers of concurrent timers or very long-running timers can consume process resources or outlive the user's expectations for the active session. <br>
Mitigation: Keep timer counts reasonable, cancel unused timers, and use an external calendar or system scheduler for critical long-term reminders. <br>
Risk: The artifact includes under-scoped API, callback, file-processing, and workflow claims that are not validated by the server security evidence. <br>
Mitigation: Treat those unrelated claims as unvalidated and rely only on the documented timer and reminder behavior unless separately reviewed. <br>


## Reference(s): <br>
- [ClawHub Timer skill page](https://clawhub.ai/thcjp/skills/timer) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and timer alert text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are session-bound reminders and process-management guidance; timer completion is expected to be relayed as user-facing text.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
