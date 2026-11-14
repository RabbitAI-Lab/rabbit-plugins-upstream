## Description:

Use the mcporter CLI to list, configure, authenticate, and call MCP servers and tools directly over HTTP or stdio, including ad-hoc servers, config edits, and CLI or type generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to operate MCP servers and tools from an agent workflow, including listing schemas, calling tools, managing auth and config, running a daemon, and generating CLI or TypeScript helpers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad MCP tool calls against HTTP and stdio servers.

Mitigation: Use trusted MCP endpoints and review target server or tool selectors before invoking them.

Risk: Stdio server commands and daemon operations can run local processes.

Mitigation: Review local commands before execution and run them only in an appropriate working directory and trust boundary.

Risk: Auth and config commands can change credentials, sessions, or server configuration.

Mitigation: Avoid passing secrets unless required, use least-privilege credentials, and inspect config changes before reuse.

Risk: The install metadata references an unpinned node package.

Mitigation: Prefer a pinned or otherwise controlled mcporter package version for repeatable deployments.

## Reference(s):

- [Mcporter homepage](http://mcporter.dev)
- [ClawHub skill page](https://clawhub.ai/seanford/skills/mcporter)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON payload examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers mcporter JSON output for machine-readable results when appropriate.]

## Skill Version(s):

1.0.0 (source: server release evidence and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
