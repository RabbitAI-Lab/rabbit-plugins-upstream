## Description: <br>
Calendar helps agents create calendar events, manage meetings, detect scheduling conflicts, and sync schedules across calendar providers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and teams use this skill to plan projects, create and manage calendar events, coordinate meetings, and view synced schedules across providers. It is not intended for personnel performance evaluation or complex enterprise attendance scheduling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags inconsistent documentation and an unclear output format. <br>
Mitigation: Confirm the intended calendar-provider scopes, side effects, and JSON output contract before installing or publishing. <br>
Risk: The skill describes write-capable calendar actions, including creating, modifying, deleting, syncing, and notifying participants. <br>
Mitigation: Require explicit user confirmation before calendar changes, participant notifications, syncs, or deletions, and grant only minimum necessary calendar permissions. <br>
Risk: The artifact requests exec access and includes a generic API key configuration example. <br>
Mitigation: Avoid broad shell execution or broad credentials unless the publisher clarifies required scopes; use scoped provider credentials where calendar access is needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/calendar) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Guidance, Configuration] <br>
**Output Format:** [JSON responses with status, summary, details, and improvement fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Calendar actions may create events, invitations, synced schedule views, meeting arrangements, and conflict checks.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
