## Description: <br>
Fomo lets an agent read, create, update, and delete Fomo data through the OOMOL connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent manage Fomo events through an OOMOL-connected account, including listing, retrieving, creating, updating, and deleting events. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete Fomo event data through the user's connected account. <br>
Mitigation: Require explicit user confirmation of the target, payload, and intended effect before running write or destructive actions. <br>
Risk: First-time setup may ask the user to install or authenticate the oo CLI. <br>
Mitigation: Review installation commands before execution and only run setup steps after a relevant command fails with an authentication, connection, or missing CLI error. <br>


## Reference(s): <br>
- [Fomo homepage](https://fomo.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Fomo skill on ClawHub](https://clawhub.ai/oomol/skills/oo-fomo) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
