## Description: <br>
Agent群组工具免费版 provides lightweight multi-agent group collaboration with group creation, agent invitations, @mentions, announcements, message archive search, and topic channels for single-instance agent teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate small multi-agent teams through familiar group-chat patterns, including temporary task groups, project collaboration, broadcasts, and archived status updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Group messages, logs, and archives may contain sensitive coordination data retained in local SQLite storage. <br>
Mitigation: Review the SQLite path, log path, message retention settings, and archive cleanup policy before use. <br>
Risk: Callback URLs or external sync options may send group data outside the local workspace. <br>
Mitigation: Avoid callback URLs and external sync options unless the destination and data handling are approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/group-agent-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI examples, YAML and Python snippets, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs describe local SQLite-backed group operations, optional callback URLs, execution logs, and error states.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
