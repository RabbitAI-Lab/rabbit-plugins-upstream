## Description: <br>
Autonomously edit videos, add captions, and remove silences via BatchEdits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chuckwhisler](https://clawhub.ai/user/chuckwhisler) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to connect OpenClaw to BatchEdits for video editing workflows, including captions, silence removal, custom style creation, upload processing, status checks, and downloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Videos selected for editing are sent to BatchEdits. <br>
Mitigation: Install and use the skill only when BatchEdits is trusted for the selected video content. <br>
Risk: API keys can be exposed if placed directly in the MCP URL. <br>
Mitigation: Prefer the header-based BATCHEDITS_API_KEY setup or OAuth flow, and avoid sharing configuration or logs that contain credentials. <br>
Risk: The upload workflow asks the agent to execute an upload command returned by BatchEdits. <br>
Mitigation: Review the command before execution and confirm it is a narrow, expected upload to BatchEdits for the intended file. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/chuckwhisler/skills/batchedits) <br>
- [Publisher Profile](https://clawhub.ai/user/chuckwhisler) <br>
- [BatchEdits MCP Endpoint](https://batchedits.com/api/mcp) <br>
- [BatchEdits OAuth Registration Endpoint](https://batchedits.com/api/oauth/register) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown with inline shell commands and MCP tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce video IDs, processing status, download guidance, and upload commands for selected local video files.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
