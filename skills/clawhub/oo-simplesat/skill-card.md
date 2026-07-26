## Description: <br>
Simplesat (simplesat.io). Use this skill for ANY Simplesat request - reading, creating, and updating data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to read Simplesat customers, surveys, questions, and responses, and to create or update customers or send survey emails through an OOMOL-connected Simplesat account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can access a connected Simplesat account through OOMOL. <br>
Mitigation: Install only when this account access is intended, and use OOMOL-scoped connections. <br>
Risk: Customer updates and survey email actions can change Simplesat state. <br>
Mitigation: Review the proposed payload and effect before approving write actions. <br>
Risk: CLI installation or login steps introduce trust and account setup decisions. <br>
Mitigation: Run install or login steps only when setup is required and OOMOL is trusted. <br>


## Reference(s): <br>
- [Simplesat Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-simplesat) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Simplesat Homepage](https://www.simplesat.io/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
