## Description: <br>
Klipfolio (klipfolio.com) skill for searching and reading Klipfolio clients, dashboards, data sources, and Klips through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent inspect account-visible Klipfolio assets through an OOMOL-connected account. It supports schema-first read actions for individual assets and lists of clients, dashboards, data sources, and Klips. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads Klipfolio assets visible to the connected account. <br>
Mitigation: Install it only when you trust OOMOL and intend the agent to access Klipfolio data through the connected account. <br>
Risk: One-time CLI install and authentication steps affect the local toolchain and OOMOL session. <br>
Mitigation: Run setup steps only after an auth, connection, billing, or missing-CLI failure, and review install or login commands before execution. <br>
Risk: A future version could add write or destructive Klipfolio actions. <br>
Mitigation: Review future releases carefully and require explicit user confirmation for any action that changes, removes, or overwrites data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-klipfolio) <br>
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Klipfolio Homepage](https://www.klipfolio.com) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before actions; read actions are safe to run directly, while any future write or destructive actions require user confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
