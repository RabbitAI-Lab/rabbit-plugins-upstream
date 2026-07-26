## Description: <br>
Manages Claude Code sessions with naming, checkpointing, and resume strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to organize long-running Claude Code work, name useful checkpoints, resume prior sessions, and troubleshoot session continuity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resumed or named sessions can carry forward sensitive context longer than intended. <br>
Mitigation: Avoid placing secrets or regulated data in sessions intended for resume, and use fresh-session controls when prior context should not carry forward. <br>
Risk: Old named sessions can accumulate stale or unnecessary work context. <br>
Mitigation: Periodically clean up named sessions that are no longer needed. <br>


## Reference(s): <br>
- [Nm Sanctum Session Management on ClawHub](https://clawhub.ai/athola/skills/nm-sanctum-session-management) <br>
- [Sanctum homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown narrative with command examples and troubleshooting guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no persistent output file is specified.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
