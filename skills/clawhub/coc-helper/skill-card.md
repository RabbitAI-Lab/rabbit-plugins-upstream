## Description: <br>
COC 7th Edition tabletop assistant for dice rolling, SAN checks, investigator management, table lookups, combat initiative, configurable rules, reproducible rolls, JSON output, and local investigator state persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiangtianjiao](https://clawhub.ai/user/jiangtianjiao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Players, Keepers, and agents supporting Call of Cthulhu 7th Edition sessions use this skill to roll dice, resolve success levels and SAN outcomes, manage investigators, generate table results, and maintain local session state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores investigator and session data locally in session.json. <br>
Mitigation: Avoid entering private real-world information in investigator names or notes, and review the local session file before sharing or publishing the skill directory. <br>
Risk: One SAN threshold helper message may be inaccurate compared with the main documented rules. <br>
Mitigation: Use the main documented SAN rules as the reference for threshold interpretation and verify edge-case SAN outcomes during play. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jiangtianjiao/skills/coc-helper) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Design proposal](artifact/PROPOSAL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Human-readable CLI text or JSON, with Markdown documentation and shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports seeded reproducible rolls and persists investigator and rules state in local session.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
