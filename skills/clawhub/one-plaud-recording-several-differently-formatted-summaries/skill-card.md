## Description: <br>
This workflow reads a Plaud recording transcript once, generates each summary format configured in Google Sheets, writes the results into a Google Doc, and logs processed recordings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and workflow operators use this skill to turn a single Plaud recording into multiple audience-specific summaries without rerunning or manually rewriting the transcript. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting recordings, transcripts, and generated summaries can contain sensitive information and may be exposed through connected Plaud, Google Docs, or Google Sheets accounts. <br>
Mitigation: Confirm the connected accounts are the intended ones before installation, and review sharing and retention settings for Plaud, Google Docs, and Google Sheets. <br>
Risk: Incorrect timezone handling can include or skip recordings outside the requested local window. <br>
Mitigation: Resolve recording windows against the user's timezone and convert Plaud timestamps before deciding whether a recording is in scope. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/one-plaud-recording-several-differently-formatted-summaries) <br>
- [AgentPMT Workflow Page](https://www.agentpmt.com/agent-workflow-skills/one-plaud-recording-several-differently-formatted-summaries) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [Get Users Current Time / Date](https://clawhub.ai/agentpmt/get-users-current-time-date) <br>
- [Google Sheets Tool](https://clawhub.ai/agentpmt/google-sheets) <br>
- [Plaud Tool](https://clawhub.ai/agentpmt/plaud) <br>
- [Google Docs Connector](https://clawhub.ai/agentpmt/google-docs-connector) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, API Calls] <br>
**Output Format:** [Markdown and plain text summaries written to Google Docs, with run status and log updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces one Google Doc per recording with sections for each configured format and appends processed recording details to Google Sheets.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
