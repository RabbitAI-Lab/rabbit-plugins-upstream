## Description: <br>
HighLevel (gohighlevel.com). Use this skill for ANY HighLevel request: reading, creating, updating, and deleting data through the OOMOL high_level connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to operate HighLevel CRM contact workflows through an OOMOL-connected account, including searching, reading, creating, updating, and deleting contacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete HighLevel CRM contacts through an OOMOL-connected account. <br>
Mitigation: Review create and update payloads before approval, and require explicit confirmation of the target contact before delete actions. <br>
Risk: First-time CLI installation and account login affect the user's OOMOL account setup. <br>
Mitigation: Run setup steps only when a command fails for an auth, connection, scope, or billing reason and only when OOMOL is trusted for the account. <br>


## Reference(s): <br>
- [HighLevel homepage](https://www.gohighlevel.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-high-level) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before execution and returns connector responses as JSON when actions run.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
