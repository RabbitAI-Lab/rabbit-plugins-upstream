## Description: <br>
Operates EasyPost through an OOMOL-connected account to create and retrieve shipping addresses, shipment trackers, carrier types, and tracker lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use this skill to manage EasyPost shipping resources through the OOMOL oo CLI. It supports reading EasyPost account data and creating immutable shipping addresses or standalone shipment trackers after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Address and tracker creation change EasyPost account state. <br>
Mitigation: Inspect the live connector schema before constructing payloads and confirm the exact payload and expected effect with the user before running write actions. <br>
Risk: Using the skill requires EasyPost access through an OOMOL-connected account. <br>
Mitigation: Only install or connect the oo CLI when the user intends to manage EasyPost through OOMOL and trusts that connected-account access path. <br>


## Reference(s): <br>
- [ClawHub EasyPost skill page](https://clawhub.ai/oomol/skills/oo-easypost) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [EasyPost homepage](https://www.easypost.com/) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before actions; write actions require explicit user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
