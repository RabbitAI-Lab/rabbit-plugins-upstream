## Description: <br>
Operate Hookdeck through an OOMOL-connected account for reading, creating, updating, and deleting Hookdeck sources, destinations, and connections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect Hookdeck connector schemas and run `oo` CLI actions for managing Hookdeck sources, destinations, and connections. It supports read workflows and confirmed write or destructive changes through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Hookdeck resources through write actions. <br>
Mitigation: Review the proposed payload and expected effect with the user before running write actions. <br>
Risk: Destructive actions can delete Hookdeck sources, destinations, or connections. <br>
Mitigation: Confirm the exact target and obtain explicit approval before running delete actions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-hookdeck) <br>
- [Hookdeck homepage](https://hookdeck.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands can return JSON from the `oo` CLI; write and destructive actions require payload review and explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
