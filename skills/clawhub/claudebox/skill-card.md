## Description:

Install and run Claude Code in a Docker-backed workspace, or connect to its HTTP, MCP, Telegram, and scheduled-job interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Claudebox to run Claude Code locally or from automation, and to configure authenticated services for remote or scheduled agent tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated HTTP or MCP endpoints can expose agent execution and workspace file control.

Mitigation: Set separate API and MCP tokens; bind services to loopback or protect them with an authenticated proxy.

Risk: Agent tasks can access host Docker or mounted credentials when run through the standard wrapper.

Mitigation: Keep untrusted prompts out of privileged runtimes; isolate workspaces and omit the Docker socket when it is unnecessary.

Risk: Installing remote scripts or using mutable images can run unreviewed code.

Mitigation: Inspect the installer and image provenance before use, and prefer pinned images and packages.

Risk: File-control operations can delete workspace files without an undo path.

Mitigation: Confirm target paths and only delete files the current task created when removal was requested.

## Reference(s):

- [Claudebox setup guide](references/setup.md)
- [Claudebox project homepage](https://github.com/psyb0t/docker-claudebox)
- [Claudebox release on ClawHub](https://clawhub.ai/psyb0t/skills/claudebox)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include text, code, and structured results from the configured runtime.]

## Skill Version(s):

2.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
