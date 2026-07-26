## Description: <br>
Upsales (upsales.com). Use this skill for ANY Upsales request - reading, creating, updating, and deleting data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and business users use this skill to read, create, update, and delete Upsales companies, contacts, and users through the oo CLI without handling raw Upsales API tokens. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Upsales records through the connected account. <br>
Mitigation: Confirm the exact payload, target record, and intended effect with the user before running write or destructive actions. <br>
Risk: The connected Upsales account may have broader permissions than the user intends for an agent workflow. <br>
Mitigation: Use an Upsales account with appropriate permissions and review the oo CLI installer before first-time setup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-upsales) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [Upsales homepage](https://www.upsales.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses oo connector schema checks before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
