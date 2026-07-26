## Description: <br>
Manage Dex personal CRM contacts, notes, reminders, and contact details through the Dex API using a DEX_API_KEY. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jaybna](https://clawhub.ai/user/jaybna) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and Clawdbot users use this skill to manage Dex CRM records from agent workflows, including searching contacts, viewing details, adding notes, creating reminders, and cleaning up newsletter-like contacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can use a Dex API key for broad read and write access to CRM contacts, notes, and reminders. <br>
Mitigation: Use only a Dex API key you are comfortable granting read/write CRM access, and confirm the exact target records before creating, updating, deleting, completing, or archiving data. <br>
Risk: The cleanup script can bulk-archive contacts based on automated newsletter and junk-contact matching. <br>
Mitigation: Run the cleanup script with --dry-run first and review the listed contacts before running it without dry-run. <br>
Risk: The scanner summary notes broad delete and bulk-archive abilities that are not clearly scoped in the main skill description. <br>
Mitigation: Review the skill and scan results before installation, and avoid delete or archive operations unless the target records are explicit and confirmed. <br>


## Reference(s): <br>
- [Dex](https://getdex.com) <br>
- [Dex API settings](https://getdex.com/settings/api) <br>
- [Dex REST API base](https://api.getdex.com/api/rest) <br>
- [ClawHub skill page](https://clawhub.ai/jaybna/skills/dex-crm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl examples, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DEX_API_KEY; destructive contact, note, and reminder operations should be confirmed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
