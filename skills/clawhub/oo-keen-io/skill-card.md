## Description: <br>
This skill lets agents use OOMOL-connected Keen IO actions to publish JSON events and query event counts or sums. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to let an agent publish Keen IO events and run count or sum analytics through OOMOL-connected credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can publish events to Keen IO collections. <br>
Mitigation: Confirm the exact add_event payload and intended effect with the user before execution. <br>
Risk: The skill depends on OOMOL as the intermediary for Keen IO actions and on persistent CLI, account, and connection setup. <br>
Mitigation: Install only when that intermediary is acceptable, and use first-time setup steps only after an auth or connection failure. <br>
Risk: Invalid payloads can fail or create unintended event structure. <br>
Mitigation: Inspect the live connector schema before constructing each action payload. <br>


## Reference(s): <br>
- [ClawHub Keen IO Skill](https://clawhub.ai/oomol/skills/oo-keen-io) <br>
- [Keen IO Homepage](https://keen.io/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before action execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
