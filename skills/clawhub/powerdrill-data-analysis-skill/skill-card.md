## Description: <br>
This skill helps an agent analyze, explore, visualize, and query data using Powerdrill by managing datasets, uploading local files, creating sessions, running natural-language analysis jobs, and retrieving charts, tables, and insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[javainthinking](https://clawhub.ai/user/javainthinking) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and analysts use this skill to connect an agent to Powerdrill for data upload, dataset management, session management, and natural-language analysis that can return narrative findings, code, tables, charts, and follow-up questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local files can be uploaded to the remote Powerdrill service for analysis. <br>
Mitigation: Confirm the exact file path and data sensitivity with the user before upload, and avoid secrets or regulated data unless the user is authorized to send it to Powerdrill. <br>
Risk: Dataset and session deletion operations can remove remote Powerdrill resources. <br>
Mitigation: Require explicit user confirmation before deleting datasets or sessions, especially when resource IDs were inferred from prior commands. <br>
Risk: Natural-language analysis queries can send user questions and dataset context to Powerdrill. <br>
Mitigation: Use only a trusted Powerdrill account and confirm before submitting analysis queries that may expose sensitive business context. <br>


## Reference(s): <br>
- [Powerdrill API Documentation](https://docs.powerdrill.ai/api-reference/v2) <br>
- [Powerdrill Quick Start Guide](https://docs.powerdrill.ai/developer-guides/quick-start-v2) <br>
- [Powerdrill Streaming Response Handling](https://docs.powerdrill.ai/api-reference/v2/streaming#streaming-response) <br>
- [Checking Powerdrill Data Source Status](https://docs.powerdrill.ai/api-reference/v2/how-to-check-data-sources) <br>
- [Powerdrill MCP Server](https://github.com/powerdrillai/powerdrill-mcp) <br>
- [Powerdrill Platform](https://chat.powerdrill.ai/) <br>
- [ClawHub Skill Page](https://clawhub.ai/javainthinking/skills/powerdrill-data-analysis-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell examples; runtime Powerdrill calls return JSON-like API responses, analysis text, code blocks, tables, chart/image URLs, citations, and follow-up questions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires POWERDRILL_USER_ID and POWERDRILL_PROJECT_API_KEY; generated table and image URLs may expire.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
