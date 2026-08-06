## Description: <br>
Calendar helps an agent handle scheduling tasks such as creating events, managing meetings, checking conflicts, and syncing calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, developers, and automation workflows can use this skill for calendar management, meeting coordination, basic scheduling, conflict checks, and calendar synchronization. It is not suitable for actual personnel performance evaluation or complex enterprise attendance scheduling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for broad read, write, and command-execution authority. <br>
Mitigation: Install it only in environments where that authority is acceptable, and review the skill before use. <br>
Risk: Calendar actions may create, change, delete, sync, or notify events unintentionally. <br>
Mitigation: Require explicit user confirmation before any calendar mutation, sync, or notification. <br>
Risk: The artifact is broad and generated rather than a tightly scoped integration. <br>
Mitigation: Treat its guidance as general scheduling assistance and verify provider-specific behavior before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with occasional JSON examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe calendar actions, configuration steps, API-key setup, troubleshooting, and review-oriented output.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
