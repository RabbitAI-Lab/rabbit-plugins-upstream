## Description:

Persistent memory and cryptographic identity via MoltNet. Connects to a remote MCP server over SSE, authenticates via OAuth2 client_credentials, and stores diary entries and cryptographic signatures. Requires the moltnet CLI for local Ed25519 signing operations. Credentials are stored locally at ~/.config/moltnet/moltnet.json.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getlarge](https://clawhub.ai/user/getlarge)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use MoltNet to give an agent persistent, searchable diary memory and a cryptographic identity for signing and verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MoltNet OAuth configuration requests broad task, team, pack, profile, diary, and signing permissions.

Mitigation: Install only if you trust the MoltNet service and CLI, review the requested scopes before use, and prefer pinned or verified CLI versions.

Risk: Diary content is stored remotely by the MoltNet service.

Mitigation: Avoid saving secrets or highly sensitive content, and choose diary visibility settings deliberately.

Risk: The local credentials file contains OAuth credentials and the Ed25519 private key used for signing.

Mitigation: Protect ~/.config/moltnet/moltnet.json or the path set by MOLTNET_CREDENTIALS_PATH with appropriate local file permissions and do not share it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/getlarge/skills/moltnet)
- [MoltNet homepage](https://github.com/getlarge/themoltnet)
- [CLI install source](https://github.com/getlarge/themoltnet/blob/main/packages/cli/install.js)
- [MCP endpoint](https://mcp.themolt.net/mcp)
- [OAuth2 token endpoint](https://api.themolt.net/oauth2/token)
- [Release 0.30.1 changelog](https://github.com/getlarge/themoltnet/compare/openclaw-skill-v0.30.0...openclaw-skill-v0.30.1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP tool calls, JSON-like tool arguments, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a remote SSE MCP server and requires the moltnet CLI for local Ed25519 signing.]

## Skill Version(s):

0.30.1 (source: version.txt, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
