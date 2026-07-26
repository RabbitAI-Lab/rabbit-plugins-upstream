## Description: <br>
Use this skill for Lodgify requests that search and read data through OOMOL's Lodgify connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and support agents use this skill to read Lodgify bookings, properties, room types, availability, and quotes through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Lodgify booking and property data through an OOMOL-connected account. <br>
Mitigation: Use it only when the user intends to read Lodgify data and trusts the OOMOL CLI and account connection model. <br>
Risk: Authentication, connection, or billing setup can enable or resume access to the Lodgify integration. <br>
Mitigation: Only run login, connection, or recharge steps after a matching command failure and clear user intent. <br>
Risk: Connector action schemas may change over time. <br>
Mitigation: Inspect the live `oo connector schema` output before building each action payload. <br>


## Reference(s): <br>
- [Lodgify homepage](https://www.lodgify.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lodgify) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
