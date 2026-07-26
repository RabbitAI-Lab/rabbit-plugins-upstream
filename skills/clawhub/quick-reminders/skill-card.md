## Description: <br>
Zero-LLM one-shot reminders (<48h) via nohup sleep + openclaw message send, operated via {baseDir}/scripts/nohup-reminder.sh. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lstpsche](https://clawhub.ai/user/lstpsche) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and personal-assistant agents use this skill to set, list, and cancel short-horizon one-shot reminders delivered through an existing OpenClaw messaging setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Detached background processes can send reminder messages later through the user's existing OpenClaw setup. <br>
Mitigation: Install only when this behavior is expected, keep reminder text low-sensitivity, and review active reminders before relying on delivery. <br>
Risk: Tampering with reminders.json can affect cleanup behavior and may cause unintended local file deletion during removal. <br>
Mitigation: Protect or review reminders.json before using remove operations, especially in shared or untrusted workspaces. <br>
Risk: Short-lived sleep-based reminders are best-effort and may be lost if the host restarts or OpenClaw is unavailable at fire time. <br>
Mitigation: Use calendar reminders or a more durable scheduler for reminders two or more days out or for critical delivery. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash command examples and natural-language reminder text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires jq and openclaw binaries; reminder delivery uses the user's existing OpenClaw messaging configuration.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
