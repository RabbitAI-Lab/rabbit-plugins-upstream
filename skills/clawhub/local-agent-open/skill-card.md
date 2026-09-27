## Description:

Helps open the local agent-skeleton assistant at http://localhost:3000, starting its server if needed and offering troubleshooting guidance when the page is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and other local assistant users can check whether the agent-skeleton page is running, open it locally, or troubleshoot startup and port conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Starting the local server may create a background process or change local files.

Mitigation: Review and confirm the proposed startup command before running it.

Risk: A different process may already be using port 3000.

Mitigation: Check which process owns the port and ask before stopping it or switching ports.

Risk: Opening the assistant outside localhost or changing network settings could expose it unexpectedly.

Mitigation: Keep access on localhost; do not change firewall, hosts, or public exposure settings without user confirmation.

## Reference(s):

- [local-agent-open on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/local-agent-open)
- [Publisher profile on ClawHub](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide opening a localhost browser page after checking server readiness.]

## Skill Version(s):

1.0.0 (source: server release metadata and manifest.json; SKILL.md frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
