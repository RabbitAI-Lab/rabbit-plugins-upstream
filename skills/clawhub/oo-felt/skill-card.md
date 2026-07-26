## Description: <br>
Felt connector skill for reading, creating, updating, and deleting Felt maps and projects through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage Felt maps and projects through the OOMOL Felt connector. It supports account reads as well as confirmed create, update, move, duplicate, and delete actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, move, duplicate, and delete Felt data through the connected account. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions. <br>
Risk: Incorrect payloads can cause unintended account changes or failed connector runs. <br>
Mitigation: Inspect the live Felt connector schema before constructing each action payload. <br>
Risk: First-time setup may require installing the oo CLI from an external URL. <br>
Mitigation: Verify the oo CLI install URL before running installation commands. <br>
Risk: Authentication, connection, scope, credential-expiration, or billing errors can block connector operations. <br>
Mitigation: Use the documented setup, connection, and billing recovery steps only after a command fails with the matching error. <br>


## Reference(s): <br>
- [ClawHub Felt skill page](https://clawhub.ai/oomol/skills/oo-felt) <br>
- [Felt homepage](https://felt.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action payload construction; command responses are JSON objects with data and metadata.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
