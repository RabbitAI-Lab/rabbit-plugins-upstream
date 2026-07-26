## Description: <br>
Google Meet helps agents create and manage meeting spaces, review conference participants, and access recordings and transcripts through AgentPMT-hosted Google Meet API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent create Google Meet spaces, manage access settings, end active conferences, and review meeting history, participants, recordings, and transcripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access sensitive Google Meet information, including transcripts, recordings, attendance data, and participant session details. <br>
Mitigation: Install only when AgentPMT and the connected Google account are trusted, use least-privilege account setup, avoid placing secrets in prompts or logs, and access meeting data only when authorized. <br>
Risk: The skill can end an active conference. <br>
Mitigation: Confirm the exact meeting space and user intent before calling the end_conference action. <br>


## Reference(s): <br>
- [Google Meet Skill on ClawHub](https://clawhub.ai/agentpmt/skills/google-meet) <br>
- [AgentPMT Google Meet Connector](https://www.agentpmt.com/marketplace/google-meet-connector) <br>
- [Google Meet Schema](schema.md) <br>
- [AgentPMT Account MCP/REST Setup](https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup) <br>
- [What AgentPMT Is](https://clawhub.ai/agentpmt/what-is-agentpmt) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions, JSON] <br>
**Output Format:** [Markdown instructions with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Remote AgentPMT tool calls return JSON for Google Meet spaces, conference records, participants, recordings, and transcripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
