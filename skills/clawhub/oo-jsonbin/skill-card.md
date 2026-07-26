## Description: <br>
Provides agent guidance for reading, creating, updating, and deleting JSONBin.io data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to read, create, update, and delete JSONBin.io bins through an OOMOL-connected account without handling raw API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete JSONBin.io records through the connected account. <br>
Mitigation: Review the exact payload and target bin before approving write actions, and require explicit approval before delete operations. <br>
Risk: Installing the skill allows the agent to operate the user's JSONBin.io account through OOMOL. <br>
Mitigation: Install it only for environments where that account access is intended, and keep the JSONBin.io connection scoped and reviewed. <br>


## Reference(s): <br>
- [JSONBin.io homepage](https://jsonbin.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jsonbin) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
