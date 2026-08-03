## Description: <br>
Captures, structures, retrieves, and safely routes notes across local markdown, Apple Notes, Bear, Obsidian, Notion, and Evernote. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to turn conversations, transcripts, decisions, projects, journal entries, and research into durable notes with owners, dates, routing, and retrieval structure. It is also used to maintain a searchable note corpus across local files and configured note platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can update or delete durable note, action, contact, and project records. <br>
Mitigation: Require previews or explicit approval for deletions, migrations, bulk edits, contact or project updates, and action sweeps. <br>
Risk: Routing notes to Notion or Evernote can send note content to external services. <br>
Mitigation: Keep routing local by default and use Notion or Evernote only after the user explicitly configures that destination. <br>
Risk: Pasted meeting or capture text may contain credentials, PINs, recovery codes, or other secrets. <br>
Mitigation: Do not store secret values; replace them with pointer-only references such as environment variables, keychain items, password-manager entries, or local config paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/notes) <br>
- [Clawic skill homepage](https://clawic.com/skills/notes) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Sensitive note handling](artifact/sensitive.md) <br>
- [Memory and storage template](artifact/memory-template.md) <br>
- [Notion platform behavior](artifact/notion.md) <br>
- [Evernote platform behavior](artifact/evernote.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration, API Calls, Guidance] <br>
**Output Format:** [Markdown notes, local files, and platform-specific commands or API payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces durable notes, action records, and routing guidance; network platform output depends on explicit user configuration.] <br>

## Skill Version(s): <br>
1.1.5 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
