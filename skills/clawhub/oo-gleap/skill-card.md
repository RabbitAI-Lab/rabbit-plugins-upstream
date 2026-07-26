## Description: <br>
Gleap helps agents read, create, update, and delete Gleap tickets and contact sessions through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to manage Gleap support tickets and contact sessions from an agent using the OOMOL oo CLI connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write actions can change Gleap tickets or contact sessions. <br>
Mitigation: Confirm the exact payload and expected effect with the user before running actions tagged as write. <br>
Risk: The delete ticket action removes a Gleap ticket by ID. <br>
Mitigation: Require explicit user approval for the exact ticket ID before running the destructive action. <br>
Risk: Connector actions depend on the connected OOMOL account and Gleap API key context. <br>
Mitigation: Use get_current_user or the live connector schema when needed to validate context before state-changing work. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-gleap) <br>
- [Gleap Homepage](https://www.gleap.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads and returns connector responses as JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
