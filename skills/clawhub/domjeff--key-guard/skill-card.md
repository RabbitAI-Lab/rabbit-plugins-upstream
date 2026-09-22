## Description:

Key Guard routes API-key checks, secret-backed API calls, and sensitive file edits through a local MCP server so raw keys stay on the user's machine.

This skill is ready for commercial/non-commercial use.

## Publisher:

[domjeff](https://clawhub.ai/user/domjeff)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Key Guard to check configured API keys, make authenticated API requests, and edit scripts or config files without exposing raw key values to the hosted model context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server gives the agent broad access to credentials, outbound requests, and local file reads/writes.

Mitigation: Use only in a tightly sandboxed environment with throwaway credentials until the server restricts allowed key names, HTTPS destinations, readable paths, writable paths, and requires explicit confirmation before secret-backed requests or file writes.

Risk: Secret-backed API calls can send credentials to destinations selected by the agent.

Mitigation: Limit the tool to approved HTTPS endpoints and require user confirmation before any request that injects a local key.

Risk: Masked read and substituted write tools can expose or modify local files if paths are not constrained.

Mitigation: Restrict readable and writable paths to the intended project directory and review masked content before writing files with substituted keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/domjeff/skills/key-guard)
- [README](artifact/README.md)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text]

**Output Format:** [Markdown guidance with shell commands, JSON MCP tool-call examples, and text MCP results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP results may include key names, validation metadata, masked file content, or API responses; raw key values are intended to remain local.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
