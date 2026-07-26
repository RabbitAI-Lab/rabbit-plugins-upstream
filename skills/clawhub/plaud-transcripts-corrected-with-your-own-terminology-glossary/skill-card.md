## Description: <br>
This skill helps agents correct new Plaud recording transcripts with a user-maintained Google Sheets terminology glossary, then write corrected transcripts, summaries, action items, correction tables, unknown-term flags, and run logs to Google Docs and Sheets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and teams use this skill to process Plaud recordings whose transcripts contain domain-specific names, numbers, formatting conventions, or terminology. The agent reads the user's glossary, corrects transcripts before summarization, writes the corrected record to Google Docs, and logs processed recordings in Google Sheets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plaud recording content, glossary terms, summaries, action items, unknown-term flags, and run metadata may be read from or written to connected Google Docs and Google Sheets. <br>
Mitigation: Use the skill only with an approved Google workspace, confirm document and sheet sharing settings, and avoid confidential or regulated recordings unless the connected storage is approved for that data. <br>
Risk: Incorrect glossary corrections could change transcript meaning or make an uncertain term look authoritative. <br>
Mitigation: Review the correction table and unknown-term flags in the generated document before relying on or sharing the corrected transcript or summary. <br>
Risk: Plaud timestamp fields can be interpreted incorrectly, causing recordings to be included in or excluded from the wrong local recording window. <br>
Mitigation: Resolve the requested window in the user's timezone and convert Plaud UTC timestamp fields before filtering recordings, as the workflow instructs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/plaud-transcripts-corrected-with-your-own-terminology-glossary) <br>
- [AgentPMT Workflow Page](https://www.agentpmt.com/agent-workflow-skills/plaud-transcripts-corrected-with-your-own-terminology-glossary) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [AgentPMT Overview](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>
- [Google Sheets Tool Skill](https://clawhub.ai/agentpmt/google-sheets) <br>
- [Plaud Tool Skill](https://clawhub.ai/agentpmt/plaud) <br>
- [Google Docs Connector Tool Skill](https://clawhub.ai/agentpmt/google-docs-connector) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with JSON examples, shell commands, corrected transcript text, summaries, action items, correction tables, unknown-term flags, and run-log entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update connected Google Docs and Google Sheets records through the user's configured AgentPMT tool connections.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
