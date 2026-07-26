## Description: <br>
Wiza (wiza.co). Use this skill for Wiza requests that read, create, or update data through an OOMOL-connected Wiza account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent operate Wiza through the OOMOL oo connector, including reading credits and reveal results, searching prospects, and starting individual contact reveals with confirmation for write actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can spend Wiza credits or create Wiza-side state. <br>
Mitigation: Confirm the exact action payload and expected effect with the user before starting an individual reveal. <br>
Risk: Setup may require installing and running the OOMOL oo CLI. <br>
Mitigation: Install or run setup only when the user needs the connector and trusts the OOMOL CLI. <br>


## Reference(s): <br>
- [ClawHub Wiza Skill](https://clawhub.ai/oomol/skills/oo-wiza) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Wiza Homepage](https://wiza.co) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return connector responses as JSON containing data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
