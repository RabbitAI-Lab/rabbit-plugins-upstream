## Description: <br>
Aha Claudecode Omc helps Claude Code with OMC choose bounded agent and capability routes for non-trivial work while keeping the main session responsible for decisions, integration, verification, and final delivery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[its-how](https://clawhub.ai/user/its-how) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers using Claude Code with OMC use this skill to decide when to stay native, when to delegate bounded search, reading, testing, review, or writing units, and how to preserve confirmation gates. It is intended for agent-side orchestration of software work rather than end-user application behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact orchestration can create unnecessary fan-out, worktree changes, persistent work, or avoidable cost. <br>
Mitigation: Require explicit confirmation before large fan-out, worktree use, persistent or autonomous work, cross-domain integration, or high-cost parallelism, and state a rollback path before proceeding. <br>
Risk: OMC or a specific OMC feature may be unavailable, stale, or different from the expected runtime surface. <br>
Mitigation: Verify Claude Code, OMC installation, agent surfaces, and feature availability before using OMC-specific delegation; skip only unavailable surfaces and disclose any fallback. <br>
Risk: Delegated lanes can expose secrets or create conflicting edits if boundaries are unclear. <br>
Mitigation: Keep secrets and session material in the primary session, assign bounded write sets to any writer, and treat delegate output as advisory evidence for final integration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/its-how/skills/aha-claudecode-omc) <br>
- [Skill metadata repository](https://github.com/its-How/aha-orch) <br>
- [OMC repository](https://github.com/Yeachan-Heo/oh-my-claudecode) <br>
- [Claude Code subagents documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands, checklists, and decision rules] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Claude Code with OMC installed for OMC-specific delegation surfaces; the skill itself is markdown-only and maintains no persistent state.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
