## Description: <br>
D&D 5e toolkit for players and DMs. Roll dice, look up spells and monsters, generate characters, create encounters, and spawn NPCs. Uses the official D&D 5e SRD API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[capt-marbles](https://clawhub.ai/user/capt-marbles) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Players and dungeon masters use this skill to roll dice, retrieve SRD spell and monster data, and generate characters, encounters, and NPCs during D&D 5e preparation or play. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local Python script when invoked. <br>
Mitigation: Review the script before installation and invoke only the documented commands. <br>
Risk: Lookup commands contact the public D&D 5e API, which can expose request paths or query terms to that external service. <br>
Mitigation: Avoid using private campaign details as lookup terms when you do not want those terms associated with the external API. <br>


## Reference(s): <br>
- [D&D 5e API](https://www.dnd5eapi.co/) <br>
- [D&D 5e API endpoint](https://www.dnd5eapi.co/api) <br>
- [ClawHub skill page](https://clawhub.ai/capt-marbles/skills/dnd) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text or JSON returned by Python CLI commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Some lookup and generation commands contact the public D&D 5e API.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
