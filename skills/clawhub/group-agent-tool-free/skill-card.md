## Description: <br>
Agent群组工具免费版 helps agents create lightweight collaboration groups, invite members, send mentions and announcements, search message archives, and organize topic channels without a complex message bus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to coordinate small multi-agent teams through group creation, membership management, targeted messages, announcements, and searchable local archives. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Group messages and archives can contain sensitive agent or business context. <br>
Mitigation: Review retention settings, local SQLite storage path, log path, and message-handling practices before using the skill with confidential data. <br>
Risk: Optional callback or external sync settings can expose group message data outside the local environment. <br>
Mitigation: Enable callbacks or external synchronization only after reviewing the destination system, credentials, and data-sharing requirements. <br>
Risk: The free edition is documented for single-instance group management and does not provide advanced enterprise controls. <br>
Mitigation: Use it for small local multi-agent teams, and avoid relying on it for cross-instance federation, enterprise permissions, end-to-end encryption, or high-availability workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/group-agent-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with CLI examples, YAML configuration, Python code examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local group-management guidance and structured response examples for agent collaboration workflows.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
