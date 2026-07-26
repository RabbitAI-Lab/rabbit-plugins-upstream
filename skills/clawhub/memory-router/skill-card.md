## Description: <br>
Memory Router helps agents manage local memory files by tiering bloated MEMORY.md content, generating focused memory manifests, auditing duplicate or revised memories, and maintaining entity and session-state indexes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jlacroix82](https://clawhub.ai/user/jlacroix82) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Memory Router to keep local agent memory files smaller, more relevant, and easier to route into a session. It is intended for workflows where an agent needs generated memory manifests, memory health checks, duplicate or conflict audits, and explicit user-controlled tiering or restore operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and writes local agent memory files, and tiering, restore, or cleanup operations can permanently modify or delete memory content. <br>
Mitigation: Install only when local memory-file management is desired, keep backups, run dry-run previews where available, and require explicit confirmation flags before destructive operations. <br>
Risk: Heartbeat or scheduled automation can write generated files such as manifests or audit reports and may be inappropriate for unattended destructive workflows. <br>
Mitigation: Schedule only reviewed low-risk commands, avoid automatic tiering or restore commands, and review generated reports before acting on them. <br>
Risk: Secrets or sensitive content stored in SESSION-STATE.md or memory files may be printed or routed into an agent transcript. <br>
Mitigation: Do not store secrets or transcript-sensitive data in memory files managed by this skill. <br>


## Reference(s): <br>
- [ClawHub Memory Router Skill Page](https://clawhub.ai/jlacroix82/skills/memory-router) <br>
- [README.md](artifact/README.md) <br>
- [INSTALL.md](artifact/INSTALL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, generated JSON manifests, and generated Markdown audit reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local memory files, manifests, backups, audit reports, entity indexes, and session-state files according to user-selected commands and configuration.] <br>

## Skill Version(s): <br>
2.4.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
