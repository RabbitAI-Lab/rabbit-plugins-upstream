## Description: <br>
Maintains a local personal address book with relationship context, contact history, important dates, meeting briefs, introductions, and privacy-aware reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and assistants use this skill to maintain a local address book, recall relationship details, prepare for meetings, manage introductions, and draft context-aware outreach without sending messages automatically. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can save and rewrite sensitive personal contact records without per-change confirmation. <br>
Mitigation: Require preview and explicit approval before saving, renaming, merging, deleting, importing, or recording sensitive facts about other people. <br>
Risk: The skill handles third-party personal information and relationship context that may be inappropriate to store in full. <br>
Mitigation: Keep the default minimal sensitive-details posture, record only facts that change future behavior, and avoid storing judgments or confidential details. <br>
Risk: Outreach nudges can surface people who should not be contacted or reminded. <br>
Mitigation: Check the suppression list before naming anyone for contact, congratulations, reminders, meeting briefs, or introductions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/people) <br>
- [Clawic Contacts skill page](https://clawic.com/skills/people) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Privacy guidance](artifact/privacy.md) <br>
- [Memory template](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown records, briefings, drafts, and configuration guidance for local contact files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Maintains local files under user-configured Clawic data paths; does not send messages.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
