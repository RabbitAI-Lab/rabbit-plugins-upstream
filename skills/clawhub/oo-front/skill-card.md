## Description: <br>
Front (front.com). Use this skill for Front requests that read, create, and update data through the OOMOL-connected front connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to operate Front contact and teammate workflows through an OOMOL-connected Front workspace, including listing, fetching, creating, and updating company contacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update Front contact data through an OOMOL connector. <br>
Mitigation: Confirm the exact payload and expected effect with the user before any write action. <br>
Risk: Connector use gives the agent access to a Front workspace through OOMOL-managed credentials. <br>
Mitigation: Install only when the user trusts OOMOL as the connector provider and intends to allow this workspace access. <br>
Risk: One-time setup commands may install or authenticate the oo CLI. <br>
Mitigation: Run install, login, or connection steps only after a matching command failure shows they are needed. <br>


## Reference(s): <br>
- [Front homepage](https://front.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-front) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
