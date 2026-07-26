## Description: <br>
Operate Agora through OOMOL's oo CLI for reading, creating, updating, and deleting Agora Console data without handling raw credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Agora Console projects and App Certificate settings through an OOMOL-connected account. It supports listing, retrieving, creating, enabling, disabling, usage lookup, and primary certificate reset workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create projects, change project status, enable or disable the primary App Certificate, and reset the primary App Certificate through a connected OOMOL account. <br>
Mitigation: Confirm the exact project, action, payload, and expected effect with the user before approving any write or destructive operation. <br>
Risk: Certificate reset is destructive and may overwrite credential material for an Agora project. <br>
Mitigation: Require explicit user approval for the target project before running reset_primary_certificate. <br>
Risk: Actions run against the user's connected OOMOL account and can affect live Agora resources. <br>
Mitigation: Use schema inspection before constructing payloads and only proceed when the connected account, project, and requested operation are clear. <br>


## Reference(s): <br>
- [Agora homepage](https://www.agora.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call the Agora connector through the oo CLI and may return JSON responses containing data and an execution ID.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
