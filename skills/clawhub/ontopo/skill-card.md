## Description: <br>
Find Israeli restaurants, check table availability across dates and venues, view menus, and produce Ontopo booking links for manual confirmation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alexpolonsky](https://clawhub.ai/user/alexpolonsky) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search Israeli restaurants, compare live table availability, inspect venue and menu details, and generate booking links that the user completes manually on Ontopo. <br>

### Deployment Geography for Use: <br>
Global; functional restaurant coverage is focused on Israel. <br>

## Known Risks and Mitigations: <br>
Risk: Availability information comes from live Ontopo website APIs and may not reflect final table availability. <br>
Mitigation: Use generated booking links only as a starting point and confirm reservation details manually on Ontopo. <br>
Risk: This is an unofficial tool that queries Ontopo using restaurant search details. <br>
Mitigation: Install only when this live-query behavior is acceptable for the intended environment. <br>
Risk: The tool provides links for manual booking rather than completing reservations. <br>
Mitigation: Do not treat CLI output as a completed booking; complete and verify any reservation on Ontopo. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alexpolonsky/skills/ontopo) <br>
- [Publisher profile](https://clawhub.ai/user/alexpolonsky) <br>
- [Ontopo website](https://ontopo.com) <br>
- [Ontopo API base](https://ontopo.com/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text or JSON CLI output, often summarized for the agent in Markdown tables.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live availability results, venue details, menu data, and booking URLs; no reservation is placed by the skill.] <br>

## Skill Version(s): <br>
1.2.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
