## Description: <br>
Northflank helps agents search and read Northflank project and service data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill when they need an agent to inspect Northflank projects and services through an OOMOL-connected account. It supports read-only project and service discovery and detail lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Northflank connection through OOMOL, which allows the agent to read project and service metadata available to that connection. <br>
Mitigation: Install and use it only for accounts where this read access is acceptable, and review the connected Northflank scopes before running actions. <br>
Risk: The first-time setup path includes a third-party CLI installer command. <br>
Mitigation: Review the oo CLI installer command or install the CLI through an approved internal process before using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-northflank) <br>
- [Northflank homepage](https://northflank.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces read-oriented Northflank connector actions and first-time setup guidance for the oo CLI.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
