## Description: <br>
Mem helps agents operate Mem notes through an OOMOL-connected account, including reading, creating, updating, searching, trashing, restoring, and deleting notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users can use this skill to have an agent manage Mem notes through an installed OOMOL connection. It supports note retrieval, search, creation, updates, trash, restore, and permanent deletion workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can access and modify Mem notes through the user's OOMOL connection. <br>
Mitigation: Use read actions only for requested note access, and confirm the exact payload and expected effect before any write action. <br>
Risk: Destructive actions can trash notes or permanently delete them. <br>
Mitigation: Require explicit user approval for the target note and operation before trashing or deleting. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live action schema before constructing each action payload. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mem) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [Mem Homepage](https://mem.ai) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Mem Icon](https://static.oomol.com/logo/third-party/mem.svg) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection; read actions may run directly, while write and destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
