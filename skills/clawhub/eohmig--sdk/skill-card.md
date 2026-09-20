## Description:

Guide users building apps, scripts, CI pipelines, or automations on top of the Codex SDK - TypeScript (`@cursor/sdk`) or Python (`cursor-sdk` / `cursor_sdk`).

This skill is ready for commercial/non-commercial use.

## Publisher:

[eohmig](https://clawhub.ai/user/eohmig)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build Codex SDK integrations in TypeScript or Python for scripts, CI pipelines, backend services, bots, and other automations. It helps choose the language and runtime, use one-shot or durable agent patterns, configure MCP servers, and handle streaming, cancellation, cleanup, and errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated integrations can launch Codex SDK agents with API keys, local repositories, cloud runtimes, and optional MCP servers.

Mitigation: Review generated code for credential scoping, explicit runtime selection, and appropriate MCP server configuration before use.

Risk: Incorrect lifecycle handling can leave SDK agents, runs, or clients open in unattended services.

Mitigation: Use context managers, `await using`, or explicit cleanup paths and confirm each run reaches a terminal result.

## Reference(s):

- [Codex SDK TypeScript docs](https://cursor.com/docs/sdk/typescript)
- [Codex SDK Python docs](https://cursor.com/docs/sdk/python)
- [Codex MCP docs](https://cursor.com/docs/mcp)
- [Cloud Agents REST API](https://cursor.com/docs/cloud-agent/api/endpoints)
- [Codex hooks docs](https://cursor.com/docs/hooks)
- [Self-hosted pool docs](https://cursor.com/docs/cloud-agent/self-hosted-pool)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline TypeScript, Python, and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include integration patterns, runtime guidance, MCP configuration advice, and error-handling recommendations.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
