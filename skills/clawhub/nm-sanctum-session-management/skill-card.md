## Description: <br>
Manages Claude Code sessions with naming, checkpointing, and resume strategies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Claude Code users and developers use this skill to name, checkpoint, resume, and troubleshoot long-running sessions across interruptions or multi-day work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Named sessions and automatic memory can retain sensitive context across conversations. <br>
Mitigation: Avoid placing credentials, regulated data, or sensitive incident details in conversations unless that retained context is acceptable. <br>
Risk: Generic triggers may surface the skill for broad session or debugging topics. <br>
Mitigation: Confirm that named-session or resume guidance is relevant before applying it. <br>
Risk: Old named sessions may preserve stale or unnecessary work context. <br>
Mitigation: Periodically clean up named sessions that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-session-management) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No generated files; provides session-management guidance and command examples.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter lists 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
