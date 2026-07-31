## Description: <br>
Octopus Deploy (octopus.com). Use this skill for ANY Octopus Deploy request - searching and reading data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, release engineers, and operations teams use this skill to search and read Octopus Deploy users, spaces, projects, environments, releases, deployments, and server tasks through an OOMOL-connected account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent may receive Octopus Deploy deployment, project, space, task, and related metadata visible to the connected account. <br>
Mitigation: Install only when the user wants Codex to read Octopus Deploy data, and review OOMOL connection scopes before use. <br>
Risk: Authentication, connection scope, expiration, or billing errors can block connector calls. <br>
Mitigation: Use the documented first-time setup and recovery steps only after commands fail with the matching error. <br>
Risk: Incorrect payloads can produce failed or misleading connector responses. <br>
Mitigation: Inspect each live action schema with the oo CLI before constructing JSON payloads. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-octopus-deploy) <br>
- [Octopus Deploy Homepage](https://octopus.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector actions return data with execution metadata; live schemas should be inspected before constructing payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: evidence.json release.version and artifact metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
