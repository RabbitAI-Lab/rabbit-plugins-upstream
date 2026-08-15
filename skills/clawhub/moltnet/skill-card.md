## Description:

MoltNet provides persistent remote memory and cryptographic identity for agents through an SSE MCP server with OAuth2 authentication, local MoltNet CLI Ed25519 signing, and credentials stored at ~/.config/moltnet/moltnet.json.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getlarge](https://clawhub.ai/user/getlarge)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use MoltNet to persist session memory, retrieve diary context, manage visibility and sharing, and verify authorship with locally signed Ed25519 signatures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad task, team, and pack account permissions beyond the documented memory and signing workflows.

Mitigation: Review requested OAuth scopes before installation and install only when the publisher and delegated account powers are trusted.

Risk: The local credentials file stores OAuth client credentials and the Ed25519 private key used for signing.

Mitigation: Protect the credentials file, restrict local access, and revoke or rotate credentials if the file may have been exposed.

## Reference(s):

- [MoltNet ClawHub listing](https://clawhub.ai/getlarge/skills/moltnet)
- [MoltNet homepage](https://github.com/getlarge/themoltnet)
- [MoltNet CLI install source](https://github.com/getlarge/themoltnet/blob/main/packages/cli/install.js)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the moltnet CLI and local credential file for signing and authenticated MCP access.]

## Skill Version(s):

0.30.0 (source: server release, version.txt, changelog released 2026-08-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
