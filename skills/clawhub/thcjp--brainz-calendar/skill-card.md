## Description: <br>
Brainz Calendar helps an agent manage Google Calendar events with gcalcli, including creating, listing, and deleting events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and other agent users use this skill to create, inspect, and delete Google Calendar events during project planning, task scheduling, and team coordination. It is not intended for personnel performance evaluation or non-Google calendar systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use shell commands to manage Google Calendar events, which may change a user's calendar if the request is too broad. <br>
Mitigation: Limit use to explicit calendar requests and review proposed commands before execution. <br>
Risk: Calendar deletion authority could remove unintended events, especially when deletion is based on a keyword. <br>
Mitigation: Require confirmation before every deletion and prefer exact event IDs, dates, or titles over broad keyword deletion. <br>
Risk: The artifact suggests a generic API_KEY without explaining why it is needed. <br>
Mitigation: Do not set a generic API_KEY unless the publisher documents the need; keep any calendar credentials scoped and out of version control. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/brainz-calendar) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with JSON status examples and shell command recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke command execution for gcalcli-based calendar operations when allowed by the agent environment.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
