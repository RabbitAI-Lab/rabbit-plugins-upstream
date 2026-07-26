## Description: <br>
Manage VibeTunnel terminal sessions. Create, list, monitor, and control terminal sessions visible in the VibeTunnel web dashboard. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[basher83](https://clawhub.ai/user/basher83) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to manage VibeTunnel-backed terminal sessions from an agent, including health checks, session creation, session inspection, input delivery, resizing, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control VibeTunnel terminal sessions and send input to running sessions. <br>
Mitigation: Keep VT_URL pointed to a trusted local or controlled server, verify the target session, and review commands before sending input. <br>
Risk: The cleanup example deletes exited sessions in bulk. <br>
Mitigation: Inspect the session list and IDs before running bulk delete commands. <br>


## Reference(s): <br>
- [VibeTunnel project](https://github.com/AugmentedMomentum/vibetunnel) <br>
- [ClawHub VibeTunnel listing](https://clawhub.ai/basher83/skills/vibetunnel) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, API calls, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses VT_URL to target a trusted VibeTunnel server and relies on vibetunnel, curl, and jq being available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
