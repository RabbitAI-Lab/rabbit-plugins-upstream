## Description:

Controls Varie Workstation sessions for starting, resuming, dispatching to, interrupting, and inspecting Claude Code coding sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[masqueradeljb](https://clawhub.ai/user/masqueradeljb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to manage local Varie Workstation coding sessions from OpenClaw channels, including routing requests, answering pending prompts, creating sessions, stopping sessions, and requesting screenshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on live coding sessions through broad workstation-control triggers.

Mitigation: Verify the target project or session before dispatching, creating, interrupting, or answering prompts, and ask the user when routing is ambiguous.

Risk: Screenshots can expose sensitive content, especially full-screen captures.

Mitigation: Use session-scoped screenshots by default, require an explicit user request for full-screen screenshots, and send captures only to the requesting user's channel.

Risk: Forwarding untrusted or mismatched text into an active session could select the wrong option or alter a task unexpectedly.

Mitigation: Map prompt responses to explicit option numbers when possible, use the chat fallback when uncertain, and avoid blind forwarding of untrusted text.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/masqueradeljb/skills/coding-agent-orchestrator)
- [Varie Workstation](https://github.com/varie-ai/workstation)
- [OpenClaw Documentation](https://docs.openclaw.ai/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline shell commands and status responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger local workstation actions and screenshot delivery when the user explicitly requests those operations.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
