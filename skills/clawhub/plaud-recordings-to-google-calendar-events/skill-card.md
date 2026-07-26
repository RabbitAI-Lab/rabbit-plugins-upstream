## Description: <br>
This skill guides an agent through scanning Plaud recordings for concrete scheduling commitments, creating matching Google Calendar events, and logging processed recordings and outcomes in Google Sheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and workflow operators use this skill to turn spoken scheduling commitments in Plaud meeting recordings into calendar events with source context. It also supports repeat runs by maintaining a Google Sheets ledger of processed recordings and created events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow reads Plaud transcripts and stores selected transcript quotes, recording links, event details, and ledger entries in connected Google services. <br>
Mitigation: Confirm the connected accounts and permissions are appropriate before use, and review generated calendar event descriptions when recordings contain sensitive meeting content. <br>
Risk: Relative dates and recording windows can be misapplied if the user's timezone or recording timestamp interpretation is wrong. <br>
Mitigation: Resolve all recording windows and spoken relative dates against the user's local timezone, then review the created events before relying on the automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/plaud-recordings-to-google-calendar-events) <br>
- [AgentPMT workflow page](https://www.agentpmt.com/agent-workflow-skills/plaud-recordings-to-google-calendar-events) <br>
- [AgentPMT account MCP/REST setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [AgentPMT overview](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions with JSON snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The workflow can create Google Calendar events and Google Sheets ledger rows through connected tools.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
