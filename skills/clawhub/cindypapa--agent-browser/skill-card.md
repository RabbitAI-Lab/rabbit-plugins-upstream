## Description:

A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cindypapa](https://clawhub.ai/user/cindypapa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to drive browser sessions through structured commands for web UI testing, data extraction, form filling, page inspection, and session workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser sessions and generated files may contain sensitive cookies, localStorage, screenshots, PDFs, traces, recordings, or saved authentication state.

Mitigation: Treat these outputs as sensitive, avoid saving privileged sessions, keep state files out of repositories, restrict permissions, and delete them when finished.

Risk: Global installation from a moving package target can change the reviewed behavior over time.

Mitigation: Prefer a pinned reviewed package version or commit instead of installing the latest global package blindly.

Risk: Broad browser automation and JavaScript execution can mutate pages, sessions, or data in unintended ways.

Mitigation: Install only in workflows where broad browser automation is appropriate and review target sites, sessions, and commands before execution.

## Reference(s):

- [ClawHub Agent Browser Skill](https://clawhub.ai/cindypapa/skills/agent-browser)
- [agent-browser CLI Repository](https://github.com/vercel-labs/agent-browser)
- [Agent Browser Skill Issues](https://github.com/TheSethRose/Agent-Browser-CLI)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with shell command examples and optional JSON-output command usage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referenced CLI can produce browser snapshots, extracted values, screenshots, PDFs, traces, recordings, and saved session state.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
