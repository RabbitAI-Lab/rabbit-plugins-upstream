## Description: <br>
Contacts maintains a local personal address book with contact notes, interaction history, upcoming dates, introductions, and privacy rules for deciding what should or should not be recorded. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and assistants use this skill to keep durable local notes about people, answer recall questions, prepare for meetings, draft relationship-sensitive messages, and maintain shared contact records without sending messages or uploading contacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores durable personal and third-party contact notes locally, which can expose sensitive relationship data if files are synced, shared, or over-collected. <br>
Mitigation: Review the local contact files periodically, keep them under the intended local Clawic paths, follow the minimization and suppression rules, and avoid storing secrets or details that should not be written down. <br>
Risk: The skill may update local address-book files directly, so incorrect merges or stale data could affect future recall. <br>
Mitigation: Review the named writes and deletions, use the stored identity keys when merging records, and audit the people and contacts files periodically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/people) <br>
- [Clawic Contacts page](https://clawic.com/skills/people) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, guidance] <br>
**Output Format:** [Plain-language responses and Markdown notes in local Clawic data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local contact data under the configured Clawic paths; it does not send messages or upload contact lists.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
