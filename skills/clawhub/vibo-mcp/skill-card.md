## Description:

vibo-mcp lets agents access Vibo event music planning through MCP to inspect events, timelines, song requests, playlists, and exports, and to perform confirm-gated updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event planners use this skill to let an agent work with Vibo event music plans, including timelines, song requests, playlists, guest participation, and music-service exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run an unpinned remote MCP package while supplying reusable Vibo credentials or captured session tokens.

Mitigation: Use a pinned, audited vibo-mcp version, store credentials or tokens in a secret manager where possible, keep MCP configuration and session files out of source control, restrict file permissions, and rotate tokens if the machine or repository is shared or compromised.

## Reference(s):

- [vibo-mcp npm package](https://www.npmjs.com/package/vibo-mcp)
- [Vibo](https://vibodj.com)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/vibo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating Vibo operations are documented as confirm-gated; compact responses strip media fields by default for selected read tools.]

## Skill Version(s):

1.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
