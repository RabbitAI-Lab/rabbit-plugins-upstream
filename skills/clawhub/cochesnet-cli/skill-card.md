## Description: <br>
Use the cochesnet CLI to search coches.net listings and fetch listing details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pjtf93](https://clawhub.ai/user/pjtf93) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to form exact cochesnet CLI commands for searching coches.net marketplace listings, retrieving listing details, and requesting JSON output for scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a separate cochesnet command being present on PATH, so a user could accidentally run an unintended local executable. <br>
Mitigation: Before installing or using the skill, confirm that the cochesnet command on PATH is the legitimate CLI intended for this workflow. <br>
Risk: Search queries and listing IDs are sent to the configured coches.net endpoint during normal CLI use. <br>
Mitigation: Use the skill only when sending that marketplace query data to the configured coches.net endpoint is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pjtf93/skills/cochesnet-cli) <br>
- [coches.net API endpoint](https://apps.gw.coches.net) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and environment variable names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include cochesnet search and listing commands, optional JSON flags, environment variable configuration, and exit-code handling.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
