## Description: <br>
Square (squareup.com). Use this skill for ANY Square request: reading, creating, and updating data through an OOMOL-connected Square account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate Square customer and seller-location workflows from an agent through the OOMOL Square connector. It supports reading customer and location data, and creating or updating customer records after user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Square customer and seller-location data through the connected OOMOL account. <br>
Mitigation: Use only trusted OOMOL and Square connections, and limit use to accounts whose customer and location data the user is authorized to access. <br>
Risk: Write actions can create or update Square customer records. <br>
Mitigation: Review the exact payload and effect with the user, then require explicit confirmation before running write actions. <br>
Risk: Connector action schemas can change over time. <br>
Mitigation: Inspect the live Square connector schema before constructing each payload so inputs match the current action contract. <br>


## Reference(s): <br>
- [ClawHub Square Skill](https://clawhub.ai/oomol/skills/oo-square) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Square](https://squareup.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, Configuration guidance, Markdown guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs agents to inspect live connector schemas before execution and to request confirmation before write actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
