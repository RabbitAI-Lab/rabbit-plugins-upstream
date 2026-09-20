## Description:

A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shifengwang333-ai](https://clawhub.ai/user/shifengwang333-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to drive browser automation for web interaction, UI testing, form filling, data extraction, and page snapshotting through the agent-browser CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved browser state, cookies, and storage can preserve authenticated sessions.

Mitigation: Store state files only in protected locations, avoid sharing them, and delete them when they are no longer needed.

Risk: Screenshots, PDFs, videos, traces, and storage dumps can capture sensitive page content.

Mitigation: Review generated artifacts before retention or sharing, protect them as sensitive records, and remove unnecessary copies.

Risk: Using browser automation on logged-in sites can expose account data or perform unintended actions.

Mitigation: Review the skill before installation, run it only against intended sites, and verify actions before executing workflows with authenticated sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shifengwang333-ai/skills/agent-browser)
- [Agent Browser CLI source referenced by artifact](https://github.com/vercel-labs/agent-browser)
- [Skill issues repository referenced by artifact](https://github.com/TheSethRose/Agent-Browser-CLI)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown guidance with shell command examples; CLI responses can be text or JSON and may save screenshots, PDFs, traces, videos, or browser state files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires node and npm; browser state, cookies, traces, screenshots, videos, and PDFs may contain sensitive site data.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
