## Description: <br>
Plaud Recordings to Google Drive Sync keeps a Google Sheet and Drive folder called "Plaud Recordings" in sync with a Plaud account by logging recordings, uploading audio, and saving transcript JSON when available. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and workflow operators use this skill to sync Plaud recordings, transcript files, and tracking metadata into Google Drive and Google Sheets through AgentPMT-hosted tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow copies Plaud recordings, transcript JSON, and metadata into Google Drive and Google Sheets, which can expose sensitive recording content if sharing or retention settings are too broad. <br>
Mitigation: Install only for accounts where this sync is intended, and review Google Drive and Google Sheets sharing and retention settings before and after running it. <br>
Risk: Recordings without Plaud transcripts may be processed through the speech-to-text service. <br>
Mitigation: Confirm that using the speech-to-text service is acceptable for the recording content before running the workflow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/agentpmt/skills/plaud-recordings-to-google-drive-sync) <br>
- [AgentPMT Workflow Page](https://www.agentpmt.com/agent-workflow-skills/plaud-recordings-to-google-drive-sync) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [AgentPMT Overview](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions with JSON and bash snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides an agent through remote tool calls that create or update Google Sheets rows, Google Drive audio files, transcript JSON files, and a run summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
