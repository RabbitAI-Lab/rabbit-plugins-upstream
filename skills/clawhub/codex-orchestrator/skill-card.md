## Description: <br>
Monitor, control, and orchestrate background Codex sessions. Use this skill to track progress, handle interruptions, and ensure task completion for long-running coding tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[microcarft](https://clawhub.ai/user/microcarft) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and coding agents use this skill to supervise long-running background Codex sessions, inspect progress, respond to prompts, resume interrupted work, and stop unresponsive runs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables broad unattended control over Codex sessions, including prompt submission and termination. <br>
Mitigation: Use it in a sandboxed repository or disposable branch, inspect logs before each submit action, and avoid generic approvals unless the prompt is clearly understood. <br>
Risk: Background Codex sessions can become hard to monitor or stop if session IDs and logs are not tracked. <br>
Mitigation: Record session IDs, review session logs regularly, and stop background sessions when work is complete. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/microcarft/skills/codex-orchestrator) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Operational guidance for monitoring, controlling, resuming, and stopping background Codex sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
