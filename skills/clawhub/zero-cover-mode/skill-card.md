## Description: <br>
Zero Cover Mode guides bug fixes through root-cause analysis, generated regression tests, closure logging, weekly reporting, and repeated-bug refactoring alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xincen0725](https://clawhub.ai/user/xincen0725) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to structure bug-fix work into a repeatable loop: environment detection, root-cause documentation, regression testing, closure archival, and optional post-release verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run live code against real project systems and make persistent local changes. <br>
Mitigation: Use it only in trusted repositories, preferably in a sandbox or staging environment, and keep version control or backups available before running generated tests or regression commands. <br>
Risk: Generated tests, regression commands, cleanup, compact, and cron-style verification may affect local files or scheduled workflows. <br>
Mitigation: Manually review generated commands and verification schedules before execution, and disable cleanup or cron-style actions unless their scope is explicitly approved. <br>
Risk: Running against production services, production databases, private customer data, or live credentials could expose or alter sensitive assets. <br>
Mitigation: Do not grant production credentials or private customer data access unless the scope has been explicitly approved; run the included sensitive-data filtering before archiving evidence. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xincen0725/skills/zero-cover-mode) <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance, Python-generated files, NDJSON records, logs, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates per-bug evidence directories, regression test files, closure logs, refactoring alerts, weekly reports, and optional cron-style verification instructions.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
