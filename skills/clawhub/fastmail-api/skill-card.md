## Description: <br>
Drives the Fastmail JMAP API for mail, search, bulk triage, sending, masked email, contacts, and calendars. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to automate Fastmail over JMAP, including mailbox search and triage, drafting and sending, masked email, contacts, calendars, incremental sync, migration, and API troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Fastmail API token can expose or modify mail, contacts, calendars, and masked email according to the scopes granted. <br>
Mitigation: Use the narrowest token scope needed for the task, keep the token in an environment variable or credential manager, and do not write credential values into local notes. <br>
Risk: Bulk mailbox operations and destructive JMAP calls can affect many messages or irreversible objects. <br>
Mitigation: State affected counts before writes, require explicit confirmation for high-impact operations, snapshot prior state, and use small batches. <br>
Risk: Local Clawic notes may retain account maps, mailbox ids, sync state, operation logs, contacts, bookings, domains, and subscription metadata. <br>
Mitigation: Review the Fastmail data folder and shared Clawic boxes periodically, and keep stored records limited to task-relevant metadata. <br>


## Reference(s): <br>
- [ClawHub Fastmail API Skill](https://clawhub.ai/ivangdavila/skills/fastmail-api) <br>
- [Clawic Fastmail API Skill](https://clawic.com/skills/fastmail-api) <br>
- [Fastmail JMAP Session Endpoint](https://api.fastmail.com/jmap/session) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, markdown, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown with inline shell commands, JMAP request examples, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses curl and jq examples, reads FASTMAIL_API_TOKEN from the environment, and stores non-credential notes under declared Clawic data paths.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
