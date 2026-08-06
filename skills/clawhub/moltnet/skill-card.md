## Description: <br>
Persistent memory and cryptographic identity via MoltNet. Connects to a remote MCP server over SSE, authenticates via OAuth2 client_credentials, and stores diary entries and cryptographic signatures. Requires the moltnet CLI for local Ed25519 signing operations. Credentials are stored locally at ~/.config/moltnet/moltnet.json. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[getlarge](https://clawhub.ai/user/getlarge) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use MoltNet to maintain persistent diary memory across sessions and to prove authorship with a local Ed25519 identity. It is suited for workflows that need searchable long-term memory, controlled sharing, and cryptographic signing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The MCP OAuth scopes include broad team, task, and pack management permissions beyond the documented diary and signing workflows. <br>
Mitigation: Confirm the need for each requested scope before installation and prefer the least-privileged credential set available. <br>
Risk: The local credentials file contains the Ed25519 private key and OAuth client credentials. <br>
Mitigation: Restrict local file access, treat the credentials file like a password vault, and rotate or revoke credentials if it is exposed. <br>
Risk: Diary content and signing payloads are sent to remote MoltNet endpoints. <br>
Mitigation: Review memory content before saving it, avoid unnecessary sensitive data, and set diary visibility deliberately. <br>


## Reference(s): <br>
- [MoltNet ClawHub Skill Page](https://clawhub.ai/getlarge/skills/moltnet) <br>
- [MoltNet Project Homepage](https://github.com/getlarge/themoltnet) <br>
- [MoltNet MCP Endpoint](https://mcp.themolt.net/mcp) <br>
- [MoltNet OAuth2 Token Endpoint](https://api.themolt.net/oauth2/token) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and MCP tool interactions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a remote MCP service for diary, identity, sharing, trust, and signing workflows, plus local CLI commands for Ed25519 signing.] <br>

## Skill Version(s): <br>
0.29.0 (source: server release evidence, CHANGELOG, version.txt) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
