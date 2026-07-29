## Description: <br>
AnySearch MCP connects agents to real-time web search, vertical domain search, parallel batch search, and public URL content extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anysearch-ai](https://clawhub.ai/user/anysearch-ai) <br>

### License/Terms of Use: <br>
Apache 2.0 <br>


## Use Case: <br>
Developers and agent users use this skill to configure AnySearch as a remote MCP provider so agents can search the web, route searches through supported vertical domains, run small batches of independent searches, and extract Markdown from public URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AnySearch receives submitted searches, extracted URLs and page content, and optional registration email or API key data. <br>
Mitigation: Use the service only for data intended to be sent to AnySearch, and avoid URL extraction on private or confidential pages. <br>
Risk: API keys can be exposed if they are pasted into shared configuration, logs, or source files. <br>
Mitigation: Store keys in environment variables or local ignored files, treat them as secrets, and rotate them periodically. <br>
Risk: Agent-initiated registration can create an account and issue a one-time plaintext API key for the supplied email address. <br>
Mitigation: Confirm with the user before registration or key persistence, and explain where login details and verification email are sent. <br>


## Reference(s): <br>
- [AnySearch MCP on ClawHub](https://clawhub.ai/anysearch-ai/skills/anysearch-mcp) <br>
- [AnySearch API Key Console](https://anysearch.com/console/api-keys) <br>
- [AnySearch MCP Endpoint](https://api.anysearch.com/mcp) <br>
- [mcp-remote](https://github.com/geelen/mcp-remote) <br>
- [supergateway](https://github.com/supercorp-ai/supergateway) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown search results, extracted page Markdown, JSON configuration snippets, and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search accepts up to 10 results, batch search accepts 1-5 queries, and URL extraction returns Markdown truncated at 50,000 characters.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
