## Description: <br>
Drives the Fastmail JMAP API for mail, search, bulk triage, sending, masked email, contacts, calendars, incremental sync, and mailbox migration while emphasizing account resolution, scoped writes, snapshots, and confirmation for high-impact operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to automate Fastmail through JMAP for mail search, triage, sending, masked email, contacts, calendars, sync, backup, and migration tasks. It is most useful when an agent needs to make precise API calls without touching the wrong account, mailbox, identity, or calendar. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Fastmail API token can grant high-impact access to mail, contacts, calendars, masked email, and related account data. <br>
Mitigation: Use the narrowest token scope needed, keep the token in FASTMAIL_API_TOKEN or another credential store, and do not write the secret value into local data files. <br>
Risk: Bulk mail, contact, calendar, masked email, or mailbox operations can affect many objects or create irreversible side effects. <br>
Mitigation: State affected counts before writes, snapshot prior state where the artifact calls for it, use account and identity checks, and require explicit confirmation for high-impact or irreversible actions. <br>
Risk: The skill records operational metadata locally for later sessions, including account IDs, mailbox IDs, identities, masked addresses, operation logs, contacts, bookings, and subscriptions. <br>
Mitigation: Review the configured ~/Clawic/data paths, keep only the metadata needed for future work, and strip credentials to pointers before anything is saved. <br>


## Reference(s): <br>
- [ClawHub Fastmail API Skill](https://clawhub.ai/ivangdavila/skills/fastmail-api) <br>
- [Clawic Fastmail API Skill](https://clawic.com/skills/fastmail-api) <br>
- [Fastmail JMAP Session Endpoint](https://api.fastmail.com/jmap/session) <br>
- [Fastmail Masked Email Capability](https://www.fastmail.com/dev/maskedemail) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with JSON request examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, and a FASTMAIL_API_TOKEN environment variable for the documented command examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
