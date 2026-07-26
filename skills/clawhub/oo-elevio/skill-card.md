## Description: <br>
Elevio connector skill for searching and reading knowledge base articles and categories through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and support teams use this skill to search, list, and retrieve Elevio knowledge base articles and categories through the OOMOL oo CLI without handling raw Elevio credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on OOMOL as the broker for the user's Elevio connection. <br>
Mitigation: Install and use it only when that brokered account connection is acceptable for the deployment. <br>
Risk: First-time setup may require installing the oo CLI and connecting an Elevio account. <br>
Mitigation: Run setup steps only after an auth, missing CLI, connection, or billing error, and follow the documented OOMOL setup flow. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-elevio) <br>
- [Elevio Homepage](https://elev.io) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId when actions are run with --json.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
