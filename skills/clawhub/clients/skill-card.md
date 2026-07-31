## Description: <br>
Manages client relationships end to end for freelancers, consultants, and agencies: qualifying leads, scoping, onboarding, scope creep, getting paid. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Freelancers, consultants, and agencies use this skill to manage commercial client relationships from lead qualification through proposals, onboarding, delivery, scope changes, payment follow-up, renewal, and offboarding. It drafts client-facing language and maintains local relationship records while leaving sending, signing, pricing commitments, and acceptance decisions to the user. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records client names, work emails, rates, proposals, invoices, approval history, and relationship notes in local Clawic folders. <br>
Mitigation: Keep those folders private and backed up, and apply the user's own retention or legal-hold policy when it is stricter than the skill's update and deletion guidance. <br>
Risk: Client onboarding can involve credentials, and storing raw credential values in local notes would expose sensitive access. <br>
Mitigation: Store only pointers to a password manager, keychain item, or environment variable, and do not paste credential values into the local data folders. <br>
Risk: Drafted proposals, pricing notes, payment escalation language, and stop-work messages can materially affect client relationships. <br>
Mitigation: Review all drafts before use; the skill drafts and records, while the user sends messages, signs agreements, sets final prices, and accepts or rejects changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/clients) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Skill Homepage](https://clawic.com/skills/clients) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown drafts, local note updates, checklists, and concise plain-text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads and writes local Clawic notes under the configured client, contact, project, and profile paths; does not send messages or commit terms on the user's behalf.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
