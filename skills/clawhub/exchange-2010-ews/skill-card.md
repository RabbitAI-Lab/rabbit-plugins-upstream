## Description: <br>
Provides Python helpers for Exchange 2010 EWS mailbox, calendar, contact, task, attachment, and out-of-office operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pes0](https://clawhub.ai/user/pes0) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to connect to Exchange 2010 EWS and automate mailbox, calendar, contact, task, attachment, and out-of-office workflows. It is intended for environments where the operator can provide and govern Exchange credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill gives an agent broad live mailbox authority. <br>
Mitigation: Use least-privilege Exchange credentials and require explicit confirmation before sending email or deleting or modifying Exchange data. <br>
Risk: Credential handling includes organization-specific defaults and a PICARD_PASSWORD versus EXCHANGE_PASSWORD mismatch. <br>
Mitigation: Remove bundled defaults and fix the credential variable mismatch before deployment. <br>
Risk: Attachment downloads can write mailbox content to local storage. <br>
Mitigation: Restrict downloads to a controlled, cleaned-up directory and review files before opening or processing them. <br>
Risk: Shared mailbox and calendar access can expose data beyond the primary account. <br>
Mitigation: Limit delegate permissions and shared mailbox access to the minimum scope needed for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pes0/skills/exchange-2010-ews) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Files, Configuration] <br>
**Output Format:** [Python return values, file downloads, and markdown or code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read, create, update, send, delete, or download Exchange data depending on the called function and account permissions.] <br>

## Skill Version(s): <br>
1.0.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
