## Description: <br>
MemberVault (membervault.co) supports reading, creating, updating, and deleting MemberVault data through the OOMOL connector instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate MemberVault through an OOMOL-connected account, including listing courses, adding users, removing product access, and deleting users when explicitly approved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can create users or grant access in the connected MemberVault account. <br>
Mitigation: Confirm the exact action payload and expected account change with the user before running any write action. <br>
Risk: Destructive actions can remove product access or permanently delete a user and associated data. <br>
Mitigation: Require explicit user approval for the named target before running remove_user or delete_user, and review the payload before execution. <br>


## Reference(s): <br>
- [MemberVault homepage](https://membervault.co/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-membervault) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
