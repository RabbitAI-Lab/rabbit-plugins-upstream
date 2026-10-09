## Description:

Mission control dashboard for OpenClaw - real-time session monitoring, LLM usage tracking, cost intelligence, and system vitals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanford](https://clawhub.ai/user/seanford)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use Command Center to monitor AI agent sessions, LLM usage, costs, system vitals, scheduled jobs, and topic state from a local dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default server startup can expose sensitive session data and dashboard controls without authentication.

Mitigation: Run it only on a trusted local machine, bind to loopback where possible, and set token, Tailscale, or Cloudflare authentication before exposing the port to any network.

Risk: Dashboard views may reveal recent agent conversations, topics, usage, costs, and workspace state.

Mitigation: Use privacy controls for demos and avoid sharing screenshots, logs, or dashboard access that include sensitive sessions or topics.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/seanford/skills/command-center)
- [GitHub Repository](https://github.com/jontsai/openclaw-command-center)
- [README](README.md)
- [Architecture Overview](docs/architecture/OVERVIEW.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs a local Node.js dashboard on port 3333; requires Node.js >=18.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and package.json report 1.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
