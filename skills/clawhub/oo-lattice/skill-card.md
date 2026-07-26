## Description: <br>
Lattice helps agents search and read Lattice users, departments, goals, and tags through an OOMOL-connected account using the oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, operators, and developers use this skill to answer Lattice questions by reading current-user, user, department, goal, and tag data through the configured OOMOL connector. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lattice may contain private employee and HR data. <br>
Mitigation: Use the skill only for explicit Lattice tasks and require confirmation before reading sensitive records, listing many users, exporting data, or making changes. <br>
Risk: Connector payloads can be wrong if built from stale assumptions. <br>
Mitigation: Inspect the live action schema with `oo connector schema` before each action and build JSON payloads from that schema. <br>
Risk: Setup and connection steps can trigger account authentication, app connection, or billing flows. <br>
Mitigation: Run setup, login, connection, or billing recovery steps only after the matching command failure. <br>


## Reference(s): <br>
- [ClawHub Lattice skill page](https://clawhub.ai/oomol/skills/oo-lattice) <br>
- [Lattice homepage](https://lattice.com) <br>
- [oo CLI repository](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
