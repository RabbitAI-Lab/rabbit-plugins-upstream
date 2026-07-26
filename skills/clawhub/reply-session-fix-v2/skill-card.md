## Description: <br>
Diagnose und dauerhaft fixen von 'reply session initialization conflicted' Errors in OpenClaw via 3-Layer-Setup (Client-Heal JS, Server Watchdog, Retry-Patch). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[raumkommer](https://clawhub.ai/user/raumkommer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to diagnose and repair OpenClaw reply-session initialization conflicts after gateway restarts or stale browser sessions. It provides a layered runbook for client-side session clearing, a server watchdog, and a gateway retry patch. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent privileged changes to nginx, systemd, root-owned OpenClaw files, and installed gateway JavaScript can be difficult to undo. <br>
Mitigation: Back up the affected OpenClaw configuration, nginx configuration, session data, and patched gateway files before applying the runbook; document the rollback steps for the watchdog, nginx injection, and retry patch. <br>
Risk: Deleting the wrong session key or deleting transcripts can remove active or important session state. <br>
Mitigation: Verify the exact session key before deletion, delete only the intended dashboard or subagent session, and never target agent:main:main. <br>
Risk: Reloading nginx or restarting the OpenClaw gateway can interrupt active users. <br>
Mitigation: Schedule service reloads or restarts during an appropriate maintenance window and confirm service health after each change. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/raumkommer/skills/reply-session-fix-v2) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/raumkommer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown runbook with shell, nginx, JavaScript, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes operational verification commands and cautions for session deletion, service reloads, and patch reapplication.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release evidence; artifact frontmatter reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
