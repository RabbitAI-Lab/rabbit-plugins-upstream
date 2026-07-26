## Description: <br>
Sage Sales Management helps agents read, create, update, and delete Sage Sales Management CRM data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Sage Sales Management CRM records from an agent, including account, contact, and opportunity lookup, listing, creation, update, and deletion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete CRM records in the connected Sage Sales Management account. <br>
Mitigation: Review write and delete requests carefully and require explicit confirmation of the exact payload, target, and expected effect before execution. <br>
Risk: The skill depends on an authenticated OOMOL connection to Sage Sales Management. <br>
Mitigation: Use setup and recovery steps only after authentication, connection, scope, expiration, app readiness, or billing errors occur. <br>


## Reference(s): <br>
- [Sage Sales Management homepage](https://www.forcemanager.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sage-sales-management) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing payloads; write and destructive actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
