## Description: <br>
PRTG Classic (paessler.com). Use this skill for ANY PRTG Classic request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to read PRTG Classic device and sensor information through an OOMOL-connected account. It helps an agent inspect live connector schemas, run read-only PRTG Classic actions, and return device or sensor status details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs shell commands through the oo CLI and depends on the user's installed CLI, sign-in state, and connected PRTG Classic account. <br>
Mitigation: Use the skill only for users authorized to access the connected PRTG Classic account, and follow the documented setup and recovery steps only after an auth or connection error. <br>
Risk: Future connector actions or user requests could involve write or destructive operations even though the listed PRTG Classic actions are read-only. <br>
Mitigation: For any action tagged write or destructive, confirm the exact target, payload, and expected effect with the user before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-prtg-classic) <br>
- [PRTG Classic homepage](https://www.paessler.com/prtg) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can guide an agent to return JSON data from read-only PRTG Classic connector actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
