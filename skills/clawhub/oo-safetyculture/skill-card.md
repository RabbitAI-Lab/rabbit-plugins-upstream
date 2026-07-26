## Description: <br>
Use SafetyCulture through OOMOL's safetyculture connector for reading, creating, and updating SafetyCulture data instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to inspect SafetyCulture actions and inspections, list and search records, and create SafetyCulture actions through an OOMOL-connected account. The skill guides the agent to fetch live connector schemas before constructing payloads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The create_action operation can change SafetyCulture state. <br>
Mitigation: Confirm the exact payload and intended effect with the user before running write actions. <br>
Risk: The skill depends on OOMOL CLI and connector access to a connected SafetyCulture account. <br>
Mitigation: Run installation, login, or connection steps only when needed and only when the user trusts the OOMOL CLI and connector setup. <br>


## Reference(s): <br>
- [ClawHub SafetyCulture skill page](https://clawhub.ai/oomol/skills/oo-safetyculture) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [SafetyCulture homepage](https://safetyculture.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash, PowerShell, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live OOMOL connector schemas before constructing action payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
