## Description: <br>
Summarize local coding work and submit selected worklog items to Perfly through the hosted Agent Sync MCP endpoint. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levi840714](https://clawhub.ai/user/levi840714) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill to turn approved local work metadata into concise Perfly worklog items. It previews proposed entries before submission unless unattended submission is explicitly enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Work summary metadata is sent to the Perfly MCP service. <br>
Mitigation: Keep preview-and-confirm enabled and submit only approved summary metadata. <br>
Risk: Sensitive project material could be included if the agent over-collects context. <br>
Mitigation: Follow the skill privacy boundary: do not submit source code, diffs, logs, secrets, customer data, document bodies, issue bodies, pull request bodies, attachments, or full terminal output. <br>
Risk: Bearer ingestion tokens may be exposed if handled in chat. <br>
Mitigation: Prefer OAuth discovery; when a token fallback is required, create it in the Perfly app setup page and do not paste tokens into chat. <br>


## Reference(s): <br>
- [Perfly](https://perfly.dev) <br>
- [Perfly MCP endpoint](https://api.perfly.dev/mcp) <br>
- [ClawHub package](https://clawhub.ai/levi840714/skills/perfly-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Markdown, Configuration] <br>
**Output Format:** [Markdown guidance with MCP tool calls and structured worklog item payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces 1 to 50 concise worklog items and metadata-only evidence references; requires user confirmation before writing unless unattended submission is enabled.] <br>

## Skill Version(s): <br>
1.0.1 (source: artifact/manifest.json and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
