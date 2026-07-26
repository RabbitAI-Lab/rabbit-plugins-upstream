## Description: <br>
Hybrid search memory system for AI agents with manual search and storage, plus optional opt-in auto-capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hargabyte](https://clawhub.ai/user/hargabyte) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI agents use this skill to store, search, and retrieve local project or team memories with hybrid ranking. Users may optionally enable local transcript auto-capture after configuring explicit source paths. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional transcript auto-capture can process sensitive local session data if broad paths are configured. <br>
Mitigation: Leave auto-capture disabled until needed, configure narrow source paths, and exclude secrets or regulated data. <br>
Risk: Installation and service setup involve shell scripts and may create persistent background processes. <br>
Mitigation: Review install.sh before running it, avoid curl-piped execution where possible, and confirm how to stop nohup or systemd processes. <br>
Risk: Local memories are stored in a user-controlled ~/.chaos database. <br>
Mitigation: Audit or delete the local database when needed and protect it with appropriate filesystem or disk-level controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hargabyte/skills/chaos-mind) <br>
- [CHAOS Mind repository](https://github.com/hargabyte/Chaos-mind) <br>
- [CHAOS Mind README](https://github.com/hargabyte/Chaos-mind/blob/main/README.md) <br>
- [Ollama](https://ollama.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and local CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local memory search, storage, listing, and optional auto-capture setup guidance.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
