## Description: <br>
Transform AI agents from task-followers into proactive partners that anticipate needs and continuously improve, with protocols for persistent memory, proactive check-ins, security hardening, and self-improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to configure agents that maintain continuity across sessions, proactively surface useful work, and apply safety checks before external or destructive actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent profile and session files may store personal details without enough consent or retention boundaries. <br>
Mitigation: Require confirmation before saving personal details, define where memory files live, and document how users can review, edit, or delete stored memory. <br>
Risk: Background email, calendar, cleanup, and heartbeat behavior may create unwanted monitoring or actions. <br>
Mitigation: Disable autonomous checks unless the user opts in, and require approval for external, public, or destructive actions. <br>
Risk: The bootstrap rule can cause the agent to follow local bootstrap instructions automatically. <br>
Mitigation: Remove or rewrite the BOOTSTRAP.md auto-follow rule so bootstrap content is inspected and confirmed before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/proactive-agent) <br>
- [Onboarding Flow Reference](artifact/references/onboarding-flow.md) <br>
- [Security Patterns Reference](artifact/references/security-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file templates, command examples, and configuration patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces agent operating guidance and workspace files for memory, onboarding, heartbeat checks, and security review.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 3.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
