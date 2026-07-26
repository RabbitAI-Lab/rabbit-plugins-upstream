## Description: <br>
NinjaPear lets agents query company intelligence and email-provider checks through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve NinjaPear company intelligence, check email provider status, inspect account credit balance, and resolve company websites through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connector calls can use the user's connected NinjaPear account and credits. <br>
Mitigation: Use the skill only for explicit NinjaPear or company-intelligence tasks, and avoid casual invocations that could trigger unwanted external lookups. <br>
Risk: Authentication, connection, or billing failures can interrupt a requested lookup. <br>
Mitigation: Run setup or billing steps only after a matching command failure and follow the documented OOMOL remediation path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ninjapear) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [NinjaPear homepage](https://nubela.co/) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector calls return JSON data with execution metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
