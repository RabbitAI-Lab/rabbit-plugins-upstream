## Description: <br>
Muse gives ClawBot access to team coding history through the tribe CLI so agents can search past sessions, use project context, manage knowledge, and orchestrate autonomous work across a codebase. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexander-morris](https://clawhub.ai/user/alexander-morris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use Muse to query coding-session history, manage a shared knowledge base, inspect prior work, and coordinate autonomous agents through the authenticated tribe CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authenticated tribe CLI may access or synchronize sensitive development history. <br>
Mitigation: Install only after approving the provider's privacy, retention, deletion, and sharing terms, and scope commands with project, current-directory, and time-range filters where possible. <br>
Risk: Coding sessions may contain secrets, regulated data, or proprietary source details. <br>
Mitigation: Avoid syncing or querying those materials unless organizational policy permits it, and redact or exclude sensitive projects before use. <br>
Risk: MUSE and CIRCUIT commands can start, prompt, monitor, or stop autonomous agents. <br>
Mitigation: Run agent-orchestration commands intentionally from an authenticated account and review agent output before applying changes. <br>


## Reference(s): <br>
- [Muse Skill on ClawHub](https://clawhub.ai/alexander-morris/skills/muse) <br>
- [TribeClaw deployment site](https://tribeclaw.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON command outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authenticated tribe CLI session; some MUSE and CIRCUIT commands require beta mode or manual TUI execution.] <br>

## Skill Version(s): <br>
1.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
