## Description: <br>
This skill helps agents use the PortEden CLI to list, search, create, update, and delete Google and Outlook calendar events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users and lightweight automation workflows use this skill to manage calendar events through natural-language agent requests backed by PortEden CLI commands. It supports listing calendars, querying events by date range or keyword, creating meetings with attendees and locations, and updating or deleting events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and change real calendar data through PortEden. <br>
Mitigation: Use a limited calendar account or profile and manually confirm each create, update, or delete target before execution. <br>
Risk: Authentication may remain available through local credentials or an API key. <br>
Mitigation: Avoid shared or highly sensitive environments, keep API keys out of scripts and version control, and log out or clear credentials after use on shared machines. <br>
Risk: The artifact claims local-only privacy, but evidence.security says cloud/API data flows are under-disclosed. <br>
Mitigation: Do not use this skill with regulated or highly sensitive calendar data unless the data-flow language is corrected and reviewed. <br>
Risk: The trigger condition mentions data analysis and reporting rather than calendar management. <br>
Mitigation: Invoke the skill only for explicit calendar tasks and verify the selected operation matches the requested calendar action. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/calendar-skill-tool-free) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline bash commands and optional JSON, text, or CSV command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read or mutate live calendar data through PortEden; FREE edition is scoped to single-task personal use.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence; artifact frontmatter lists 1.0.1 and body lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
