## Description: <br>
Recruitee helps agents operate Recruitee through an OOMOL-connected account for reading offers, searching candidates, and creating candidates with confirmation for write actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Recruiting teams and agents use this skill to retrieve Recruitee offers, search candidate records, and create candidates through an OOMOL-connected Recruitee account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read actions may expose Recruitee offer and candidate information in the conversation. <br>
Mitigation: Use the skill only for intended Recruitee work and avoid requesting unnecessary candidate or offer details. <br>
Risk: The create_candidate action changes Recruitee state. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running the write action. <br>
Risk: First-time setup, authentication, connection, or billing steps may be needed before the connector can run. <br>
Mitigation: Run setup or connection steps only after the matching command failure and follow the documented OOMOL connection guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-recruitee) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Recruitee homepage](https://recruitee.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read actions can return Recruitee offer and candidate data; write actions require user confirmation of the exact payload and effect.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
