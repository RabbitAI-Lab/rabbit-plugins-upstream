## Description:

Headless browser automation CLI optimized for AI agents with accessibility tree snapshots and ref-based element selection

This skill is ready for commercial/non-commercial use.

## Publisher:

[unfall103-debug](https://clawhub.ai/user/unfall103-debug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to drive repeatable browser workflows, inspect accessibility-tree snapshots, select elements by stable refs, and manage isolated sessions for web automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved authentication state, cookies, and localStorage can expose sensitive account access.

Mitigation: Treat saved state files and browser storage output like credentials: keep them out of source control and shared workspaces, redact logs, and delete them when no longer needed.

Risk: Browser automation in authenticated sessions can perform unintended actions on live web applications.

Mitigation: Review target URLs and proposed commands before execution, use isolated sessions, and prefer least-privileged accounts for automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/unfall103-debug/skills/agent-browser)
- [agent-browser project homepage](https://github.com/vercel-labs/agent-browser)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce browser artifacts such as screenshots, PDFs, saved state files, cookies, storage values, and network request summaries.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
