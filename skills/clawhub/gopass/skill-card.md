## Description: <br>
Helps agents store, retrieve, list, and manage secrets using gopass, including CRUD operations, secret generation, TOTP, recipients, mounting stores, and clipboard operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erdgeclaw](https://clawhub.ai/user/erdgeclaw) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators who use gopass can use this skill to operate password stores, including searching entries, showing secrets, creating or updating entries, generating passwords, managing recipients, mounting stores, syncing stores, and retrieving TOTP codes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reveal or copy secrets, including passwords and TOTP codes. <br>
Mitigation: Require explicit confirmation before revealing or copying secrets, and avoid clipboard use on untrusted systems. <br>
Risk: The skill can overwrite, delete, recursively delete, change recipients, or sync password-store data. <br>
Mitigation: Confirm the exact action and scope before execution, and verify Git remotes and access controls before syncing or changing recipients. <br>
Risk: Auto-confirm and warning-suppression flags can bypass normal safety prompts. <br>
Mitigation: Avoid auto-confirm or warning-suppression flags unless the exact action and scope have already been approved. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include commands that reveal, copy, modify, delete, sync, or change access to secrets; users should confirm sensitive operations before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
