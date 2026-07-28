## Description: <br>
Daily (daily.co) lets an agent read, create, update, and delete Daily rooms and meeting tokens through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and operators use this skill to manage Daily room lifecycle, meeting token, and domain configuration workflows from an agent while relying on an OOMOL-connected Daily account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing Daily actions can create meeting tokens, create rooms, update rooms, or delete rooms. <br>
Mitigation: Review the exact payload and intended effect with the user before approving write actions, and require explicit approval before deleting a room. <br>
Risk: The skill depends on the oo CLI and an OOMOL-connected Daily account. <br>
Mitigation: Install and use the skill only when the user trusts the oo CLI installer, their OOMOL account connection, and the Daily account being managed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-daily) <br>
- [Daily Homepage](https://www.daily.co/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses the Daily connector through the oo CLI and requires user confirmation before write or destructive operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
