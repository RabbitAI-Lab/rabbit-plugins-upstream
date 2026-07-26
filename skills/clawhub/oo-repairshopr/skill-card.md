## Description: <br>
RepairShopr (repairshopr.com). Use this skill for ANY RepairShopr request - searching and reading data through the OOMOL oo CLI connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to inspect RepairShopr account, customer, and ticket data through an OOMOL-connected account. It guides agents to inspect the live connector schema, run read actions with JSON payloads, and fall back to setup steps only after an authentication or connection failure. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads RepairShopr customer and ticket data from a connected account. <br>
Mitigation: Install and use it only when comfortable with OOMOL's oo CLI and the connected RepairShopr account, as recommended by the security guidance. <br>
Risk: The oo CLI installer and account connection are prerequisites outside the skill artifact. <br>
Mitigation: Review the oo CLI installer and OOMOL account connection before first use. <br>
Risk: Future expansion could add RepairShopr write or destructive actions. <br>
Mitigation: Require explicit user approval for any future write or destructive RepairShopr action and its exact payload. <br>


## Reference(s): <br>
- [RepairShopr homepage](https://www.repairshopr.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-repairshopr) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses schema-first oo CLI commands and read-only RepairShopr connector actions documented by the skill.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
