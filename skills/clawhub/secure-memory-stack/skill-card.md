## Description: <br>
A secure local memory system combining Baidu Embedding semantic search, Git Notes structured storage, and filesystem-based memory management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xqicxx](https://clawhub.ai/user/xqicxx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to initialize, configure, search, maintain, and diagnose a local memory stack that combines semantic search, Git Notes, and Markdown/file storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Memory content or search queries may be sent to Baidu when embedding features are enabled, despite local-storage claims. <br>
Mitigation: Use the skill only when comfortable with Baidu embedding processing, and avoid storing secrets or highly sensitive notes unless true offline behavior is independently verified. <br>
Risk: Backup and restore operations are high-impact because they can overwrite or expose local memory data. <br>
Mitigation: Protect backup directories, review restore sources, and restore only from trusted backups. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xqicxx/skills/secure-memory-stack) <br>
- [DOCUMENTATION.md](DOCUMENTATION.md) <br>
- [INSTALLATION.md](INSTALLATION.md) <br>
- [MEMORY_SYSTEM_GUIDE.md](MEMORY_SYSTEM_GUIDE.md) <br>
- [QUICK_START.md](QUICK_START.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files, Git Notes data, configuration files, logs, and backups during use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, package.json, CHANGELOG released 2026-01-31) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
