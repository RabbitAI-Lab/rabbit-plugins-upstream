## Description: <br>
Google 日历基础版 helps an agent manage personal Google Calendar events with gcalcli, including listing date ranges, creating events, deleting matched events, and using CalDAV backup paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal productivity users use this skill to have an agent inspect, create, and clean up calendar events from natural-language requests. It is suited to lightweight personal calendar workflows that can tolerate command-line calendar tooling and manual review before destructive changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Calendar deletion authority can remove matched events without enough confirmation context. <br>
Mitigation: Require the agent to preview matched events and obtain explicit user approval before deletion. <br>
Risk: Calendar and CalDAV operations contact external services despite artifact text claiming local-only privacy. <br>
Mitigation: Treat Google Calendar or CalDAV access as external data sharing and approve only trusted service endpoints. <br>
Risk: Calendar credentials and command-line tooling may expose sensitive schedule data to the agent runtime. <br>
Mitigation: Install only when command-line access to calendar tooling and credentials is acceptable, and keep credentials out of logs and shared files. <br>
Risk: Optional callback URLs may send completion data to untrusted destinations. <br>
Mitigation: Avoid untrusted callback URLs and review any callback destination before use. <br>


## Reference(s): <br>
- [ClawHub skill page: brainz-calendar-tool-free](https://clawhub.ai/thcjp/skills/brainz-calendar-tool-free) <br>
- [Publisher profile: thcjp](https://clawhub.ai/user/thcjp) <br>
- [Source skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include structured JSON result examples, execution logs, and command-line calendar operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
