## Description: <br>
Drafts, edits, and rewrites prose in the user's own voice for emails, posts, essays, memos, proposals, social copy, and similar writing tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and individual writers use this skill to draft, revise, shorten, restructure, and proof prose while preserving a user's voice, style rules, contact preferences, and project context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent writing, contact, and project memory may be created or changed under ~/Clawic/data/. <br>
Mitigation: Review the skill before installing, use a configuration that requires confirmation before saving or deleting durable data, and inspect the affected Clawic data folders regularly. <br>
Risk: Stored writing profiles and contact/project records may contain sensitive style preferences, personal context, or third-party details. <br>
Mitigation: Keep credentials out of ~/Clawic/data/, replace secret values with pointers, and avoid storing third-party personal data beyond what is necessary for the writing task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/writing) <br>
- [Clawic Writing skill page](https://clawic.com/skills/writing) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Working file templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown or plain text drafts, edits, rewrites, and concise editorial guidance; persistent profile files are Markdown or YAML.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update local writing, contact, and project profile files under ~/Clawic/data/.] <br>

## Skill Version(s): <br>
1.1.1 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
