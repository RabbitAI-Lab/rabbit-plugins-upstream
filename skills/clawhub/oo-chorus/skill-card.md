## Description: <br>
Chorus (chorus.ai). Use this skill for ANY Chorus request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and business users with an OOMOL-connected Chorus account use this skill to search and read Chorus conversations, teams, engagements, scorecards, and current-user details through the oo CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read Chorus conversations and business records visible to the connected account. <br>
Mitigation: Install it only for agents and users that should access that Chorus account, and rely on Chorus and OOMOL account permissions to limit scope. <br>
Risk: Setup may require installing or signing into the oo CLI and connecting Chorus in OOMOL. <br>
Mitigation: Run setup steps only after CLI, authentication, or connection errors, and review the destination before opening connection or billing links. <br>
Risk: Payloads built from assumptions can be invalid or request unintended fields. <br>
Mitigation: Fetch the live action schema with `oo connector schema` before constructing each action payload. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chorus) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Chorus homepage](https://www.chorus.ai) <br>
- [oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads; connector results are JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Chorus data is limited to records visible to the connected account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
