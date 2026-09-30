## Description:

Guides agents in running Codex, Claude, and agy/Antigravity headlessly through the acpx ACP CLI, including launch, session, troubleshooting, permission, completion, teardown, MCP, and failure-handling guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and automation operators use this skill to dispatch and supervise headless coding agents through acpx, especially when launching sessions, recovering from failed commands, checking completion, or avoiding session and permission pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Headless coding agents launched through acpx can perform high-trust automation, including file changes in the selected working directory.

Mitigation: Install only for intended headless-agent workflows, use isolated working directories, and avoid secret-heavy or regulated repositories unless the selected provider and model are approved for that data.

Risk: Persistent acpx sessions can leave resident agent and adapter processes running after a turn completes.

Mitigation: Prefer one-shot exec where possible and close persistent sessions after use.

Risk: Successful-looking exits may still hide content-filter stops, MCP initialization failures, or truncated work.

Mitigation: Read the stream or require a result file, and check logs for failure messages before trusting completion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tenequm/skills/acpx-faq)
- [Skill homepage](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [acpx project](https://github.com/openclaw/acpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; users should verify command syntax against the installed acpx CLI reference.]

## Skill Version(s):

0.6.1 (source: skill metadata, changelog released 2026-09-22, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
