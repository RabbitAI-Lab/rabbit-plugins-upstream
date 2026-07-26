## Description: <br>
Run SerpAPI searches via SerpAPI's MCP server using mcporter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[merlintxu](https://clawhub.ai/user/merlintxu) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to run SerpAPI web searches through an MCP endpoint and receive the full SerpAPI JSON response. It can also enrich AI Overview results and optionally record query and result summaries in Airtable when logging is enabled. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and results are sent to SerpAPI, and optional Airtable logging can persist full query and result payloads. <br>
Mitigation: Avoid sensitive searches when logging is enabled, keep SERP_LOG_AIRTABLE disabled unless logging is intentional, and use a least-privilege Airtable token scoped to the intended base and table. <br>
Risk: The skill depends on the globally installed mcporter npm package to call the MCP endpoint. <br>
Mitigation: Verify the mcporter package before installing it globally and keep SerpAPI and Airtable credentials in environment configuration rather than repository files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/merlintxu/skills/serpapi-mcp) <br>
- [SerpAPI Google AI Overview API](https://serpapi.com/google-ai-overview-api) <br>


## Skill Output: <br>
**Output Type(s):** [json, shell commands, configuration] <br>
**Output Format:** [JSON to stdout with optional Airtable record writes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires mcporter and SerpAPI credentials; optional Airtable logging can store full query and result payloads.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
