## Description: <br>
Runs a CRM: contacts, companies, deals, pipeline stages, follow-ups, and the data hygiene that keeps it usable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, teams, and operators use this skill to set up, maintain, audit, and operate CRM workflows for contacts, companies, deals, follow-ups, imports, migrations, pipeline reviews, and compliance-sensitive deletion or opt-out requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persistently change or delete contact, deal, import, metric, project, and shared contact records under ~/Clawic/data/. <br>
Mitigation: Use explicit confirmation for imports, merges, deletions, migrations, inbox sync, and shared-contact changes, and keep dated exports before bulk operations. <br>
Risk: CRM records may contain personal data about third parties and may be subject to opt-out, deletion, retention, or consent obligations. <br>
Mitigation: Check do-not-contact.md before contact suggestions, suppress before deleting, record request handling, and keep CRM notes limited to necessary relationship context. <br>
Risk: Automation or inbox sync can amplify stale, duplicate, or non-consented data into incorrect records or unwanted outreach. <br>
Mitigation: Prefer detection and reminders over automated outbound actions, dedupe and bounce-sweep before automation, and store email metadata instead of message bodies unless the body records a decision. <br>
Risk: Credentials for CRM APIs or logging addresses could be exposed if pasted into saved CRM files. <br>
Mitigation: Store only credential pointers such as env vars or secret-manager locations, and strip token values, signed URLs, webhook secrets, and BCC-to-CRM addresses before writing. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/crm) <br>
- [CRM Skill Homepage](https://clawic.com/skills/crm) <br>
- [CRM Skill Definition](artifact/SKILL.md) <br>
- [Pipeline Guidance](artifact/pipeline.md) <br>
- [Follow-Up Guidance](artifact/followup.md) <br>
- [Hygiene Guidance](artifact/hygiene.md) <br>
- [Import and Migration Guidance](artifact/import.md) <br>
- [Privacy Guidance](artifact/privacy.md) <br>
- [Automation Guidance](artifact/automation.md) <br>
- [Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured tables, checklists, file paths, and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to create, update, or delete CRM and shared contact records under the user's local Clawic data directories.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
