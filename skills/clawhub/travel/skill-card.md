## Description: <br>
Travel maintains a local travel archive for destinations, passports and visas, day counts, bookings, budgets, disruption notes, health needs, companions, loyalty, and post-trip debriefs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and their agents use this skill as a standing system of record for travel decisions and records, especially when checking entry constraints, recording reservations and deadlines, preparing for disruptions, estimating total costs, or closing the loop after a trip. It advises and records local notes, but does not execute purchases, bookings, cancellations, or other travel transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify sensitive local records across travel, booking, health, contact, pet, vehicle, and finance folders. <br>
Mitigation: Review configured data paths before installation, keep backups, and ask the agent to preview or summarize file changes before saving them. <br>
Risk: The skill can update or delete shared local records that it believes it wrote. <br>
Mitigation: Require change previews for shared booking and archive files, and verify identity keys before accepting deletions or row updates. <br>
Risk: Travel records may include sensitive identifiers, documents, or credentials if users paste them into the session. <br>
Mitigation: Store pointers to secure locations instead of full secrets, and keep only non-secret metadata such as issuing country, expiry dates, and last four digits where needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/travel) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Travel skill page](https://clawic.com/skills/travel) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance and local plain-text travel records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, update, and delete local records in configured Clawic data folders; users should review durable changes before relying on them.] <br>

## Skill Version(s): <br>
1.0.2 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
