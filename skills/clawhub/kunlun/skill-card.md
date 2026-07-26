## Description: <br>
Kunlun is a legacy ClawHub package for klyc-pmm private memory management that directs users to install klyc-pmm and includes scripts for agent memory backup, search, synchronization, and recovery through ai.syln.cn. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sylncn](https://clawhub.ai/user/sylncn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this legacy package to migrate from Kunlun to klyc-pmm. If they run the bundled scripts, the package can initialize cloud-backed memory, search and sync memory indexes, back up identity files, and recover memories using ai.syln.cn. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the package can send memories, identity files, and recovery tokens to ai.syln.cn. <br>
Mitigation: Install or run it only if the user intends to use that cloud-backed memory service and trusts it with those files and tokens. <br>
Risk: The security evidence says the package can change persistent behavior files. <br>
Mitigation: Review setup actions before execution and avoid running setup or backup commands unless persistent SOUL.md or HEARTBEAT.md changes are acceptable. <br>
Risk: The package is presented as a migration notice but still contains active backup, recovery, synchronization, and behavior-rule scripts. <br>
Mitigation: Prefer the stated migration path to klyc-pmm and do not execute bundled scripts unless their behavior has been reviewed. <br>
Risk: Artifact documentation says client-side encryption can fall back to plaintext transmission when encryption support is unavailable. <br>
Mitigation: Confirm the runtime has the expected encryption dependencies before pushing sensitive memory content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sylncn/skills/kunlun) <br>
- [Security documentation](artifact/SECURITY.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [klyc-pmm documentation](https://ai.syln.cn/skills/klyc-pmm) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command output and JSON recovery or index files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scripts may write local configuration, memory index, recovery, SOUL.md, or HEARTBEAT.md files when executed.] <br>

## Skill Version(s): <br>
7.0.1 (source: server release metadata, SKILL.md frontmatter, skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
