## Description: <br>
WorkBuddy Desktop session callback skill that lets an agent, cron job, or local process wake a specified WorkBuddy session and inject a message so the target agent continues with its existing context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onesfuture](https://clawhub.ai/user/onesfuture) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators using WorkBuddy Desktop use this skill to notify or resume a known live session after monitoring events, scheduled automation, asynchronous task completion, or multi-session handoff. It is intended for local WorkBuddy Desktop sessions and is not applicable to OpenClaw, CodeBuddy CLI, or other agent platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cross-session prompt injection can wake another live WorkBuddy session and trigger agent behavior without built-in target opt-in. <br>
Mitigation: Use the skill only for intentional local automation, target known session IDs, and require confirmation or allowlist controls for sensitive or recurring callbacks. <br>
Risk: Untrusted or dynamically generated callback text could cause unintended actions in the target session. <br>
Mitigation: Use fixed, trusted callback messages and avoid feeding external input directly into the callback script. <br>
Risk: Exposing callback endpoints beyond the local machine would broaden access to session injection behavior. <br>
Mitigation: Keep endpoints on 127.0.0.1 and do not expose WorkBuddy ACP endpoints to a network or container boundary. <br>


## Reference(s): <br>
- [WorkBuddy session callback ACP protocol reference](references/api_reference.md) <br>
- [ClawHub skill page](https://clawhub.ai/onesfuture/skills/workbuddy-skill-session-callback) <br>
- [GitHub issues](https://github.com/onesfuture/workbuddy-skill-session-callback/issues) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, code, configuration] <br>
**Output Format:** [Markdown guidance with shell commands and Python callback usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local WorkBuddy callback instructions and command invocations for a specified target session ID and message.] <br>

## Skill Version(s): <br>
1.0.5 (source: evidence.release.version and clawhub.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
