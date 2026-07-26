## Description: <br>
Crunchbase (crunchbase.com). Use this skill for ANY Crunchbase request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search Crunchbase organizations, autocomplete entities, and retrieve organization records through an OOMOL-connected Crunchbase account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL's oo CLI and an OOMOL-connected Crunchbase account. <br>
Mitigation: Before first use, confirm trust in OOMOL and the oo CLI installer, and connect only a Crunchbase account suitable for use through that service. <br>
Risk: Commands may fail when authentication, connection scope, app readiness, or billing requirements are not met. <br>
Mitigation: Use the documented recovery steps only after a matching failure, and avoid repeated sign-in or connection flows during normal use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-crunchbase) <br>
- [Crunchbase](https://www.crunchbase.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Crunchbase action responses are JSON when the oo CLI is run with --json.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill frontmatter metadata and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
