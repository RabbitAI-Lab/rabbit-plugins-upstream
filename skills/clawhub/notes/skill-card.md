## Description: <br>
Captures, structures, and retrieves notes in local markdown, Apple Notes, Bear, Obsidian, Notion, or Evernote. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to capture, organize, retrieve, and maintain durable notes, action items, decisions, project records, journals, and research notes across local markdown and supported note platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist and mutate durable notes, action trackers, contacts, projects, indexes, and review files with too little user confirmation. <br>
Mitigation: Require explicit confirmation before shared contacts or projects, network platforms, indexes, archive or deletion flows, and any multi-file update are created or changed. <br>
Risk: Network note platforms can receive note titles, content, searches, and filters when a note type is routed to them. <br>
Mitigation: Use network platforms only after the user routes the note type there, and prefer local markdown for sensitive or long-lived records. <br>
Risk: Credentials or sensitive personal details may be present in pasted source material intended for notes. <br>
Mitigation: Redact before writing, store only credential pointers such as environment variables or keychain locations, and state what was removed. <br>
Risk: Bulk archive, migration, sync repair, deletion, or merge work can alter many files or lose note content. <br>
Mitigation: Name the affected files or counts before running, keep rollback copies where applicable, verify counts or restore results, and confirm destructive changes first. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/notes) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Skill homepage](https://clawic.com/skills/notes) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Sensitive notes guidance](artifact/sensitive.md) <br>
- [Sync and backups guidance](artifact/sync.md) <br>
- [Migration guidance](artifact/migration.md) <br>
- [Notion platform guidance](artifact/notion.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notes, structured text, configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local note files, indexes, action trackers, contact pointers, project pointers, and platform records when the user has routed a note type to a supported platform.] <br>

## Skill Version(s): <br>
1.1.4 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
