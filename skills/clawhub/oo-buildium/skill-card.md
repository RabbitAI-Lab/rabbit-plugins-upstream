## Description: <br>
Buildium helps agents search and read Buildium rental owners, properties, units, and property notes through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent retrieve read-only Buildium rental data through the OOMOL oo connector after the account is connected. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read data from the user's connected Buildium account through OOMOL. <br>
Mitigation: Install it only for users who want agent access to that account, and keep Buildium/OOMOL permissions limited to data they are comfortable exposing. <br>
Risk: Future versions could add write or destructive Buildium actions. <br>
Mitigation: Review future releases before deployment and require explicit user confirmation for any tagged write or destructive action. <br>
Risk: First-time setup may require installing the oo CLI or reconnecting Buildium. <br>
Mitigation: Run setup steps only after a matching auth, connection, or missing-command failure, and use the published OOMOL installation and connection URLs. <br>


## Reference(s): <br>
- [ClawHub Buildium Skill](https://clawhub.ai/oomol/skills/oo-buildium) <br>
- [Buildium Homepage](https://www.buildium.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
