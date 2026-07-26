## Description: <br>
OpenClaw skill for the agent-browser CLI (Rust-based with Node.js fallback) enabling AI-friendly web automation with snapshots, refs, and structured commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[codedao12](https://clawhub.ai/user/codedao12) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to plan browser automation with the agent-browser CLI, including snapshot-based navigation, ref-driven actions, JSON-oriented workflows, and operational guardrails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation can access sensitive pages, session state, or local resources if powerful options are enabled. <br>
Mitigation: Use strict domain allowlists, block localhost and private networks, avoid local file access by default, and require explicit human approval for eval, custom runtimes, proxies, traffic interception, downloads, or credential and session changes. <br>
Risk: Saved browser state, cookies, credentials, or logs can expose secrets. <br>
Mitigation: Use ephemeral sessions where possible, keep saved login state minimal and protected, and redact tokens from logs and outputs. <br>
Risk: Unpinned or unreviewed external CLI installs can introduce supply-chain risk. <br>
Mitigation: Install a trusted pinned version in a dedicated low-privilege environment and review upgrades before use. <br>


## Reference(s): <br>
- [Agent Browser Overview](references/agent-browser-overview.md) <br>
- [Agent Browser Command Map](references/agent-browser-command-map.md) <br>
- [Agent Browser Safety](references/agent-browser-safety.md) <br>
- [Agent Browser Workflows](references/agent-browser-workflows.md) <br>
- [Agent Browser Troubleshooting](references/agent-browser-troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and operational checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory command sequences and guardrails; the skill does not execute browser automation by itself.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
