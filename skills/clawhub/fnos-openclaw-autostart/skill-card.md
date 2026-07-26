## Description: <br>
Adds a manual FnOS OpenClaw patch that starts openclaw-gateway on boot and adds a management-page toggle for autostart. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lolisaikou](https://clawhub.ai/user/lolisaikou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and FnOS/OpenClaw operators use this skill to apply and verify an autostart patch for OpenClaw gateway, including a persistent UI toggle and rollback path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manual edits to deployed OpenClaw/FnOS files can interrupt the monitor or gateway service. <br>
Mitigation: Take the documented backups first, plan for a brief monitor restart, and restore the .bak files if the patch fails. <br>
Risk: FnOS application updates can overwrite the patched server and UI files. <br>
Mitigation: Recheck the patched files after updates and reapply the skill's patch steps only after confirming the current insertion points. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lolisaikou/skills/fnos-openclaw-autostart) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands and code snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes manual backup, validation, restart, update-reapply, and rollback steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
