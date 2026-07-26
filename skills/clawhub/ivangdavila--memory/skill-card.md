## Description: <br>
Memory helps an agent remember, recall, update, and organize durable user facts in plaintext markdown files under ~/Clawic/data/memory/. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to maintain a durable local memory store for facts, decisions, people, projects, and preferences that should survive beyond a single session. It guides capture, recall, correction, deletion, import, sync, and maintenance workflows for that store. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores long-lived facts in plaintext markdown on the user's machine, so sensitive personal information or credentials could be exposed to local users, backups, sync providers, or other processes. <br>
Mitigation: Do not store secrets; store pointers to secure locations instead, apply the documented sensitive-topic boundaries, and place the memory directory on encrypted storage when the user needs stronger local protection. <br>
Risk: Deletion requests may leave traces in built-in agent memory, cloud version history, git history, or system backups outside this skill's direct control. <br>
Mitigation: Scope deletion explicitly, remove matching files, index rows, and inbound links, report removed paths, and tell the user when external histories or backups may still retain copies. <br>
Risk: Bulk maintenance, migration, rename, or index-repair commands can damage or misroute the memory store if run without review. <br>
Mitigation: Keep delete_policy set to confirm for removals, inspect affected file lists before bulk edits, and use git or another backup before large maintenance or migration operations. <br>
Risk: Stale, duplicate, or inferred facts can cause the agent to recall misleading information as if it were current. <br>
Mitigation: Record every fact with a date and source marker, use one canonical home per fact, supersede changed facts, delete facts that were never true, and run the documented search and integrity checks when recall misses or conflicts appear. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/memory) <br>
- [Memory Skill Homepage](https://clawic.com/skills/memory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, local file paths, and memory entry templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce exact write, search, maintenance, and deletion steps for plaintext files under ~/Clawic/data/memory/.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
