## Description: <br>
Gem helps agents search and read Gem CRM data through an OOMOL-connected account using the oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect Gem connector schemas and run read-oriented Gem CRM actions such as listing candidates, projects, sequences, users, and custom fields. It is intended for users with an OOMOL-connected Gem account and appropriate Gem access scopes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The agent can read Gem CRM data available to the connected OOMOL account. <br>
Mitigation: Install and use the skill only when CRM read access is intended, and review Gem and OOMOL scopes before connecting or refreshing credentials. <br>
Risk: First-time setup may require installing the oo CLI and connecting a Gem API key in OOMOL. <br>
Mitigation: Run setup only after an auth, connection, scope, credential, or missing-CLI failure, and use the documented OOMOL setup path for the Gem connection. <br>
Risk: Invalid connector payloads can cause failed requests or unexpected reads. <br>
Mitigation: Inspect the live connector schema with `oo connector schema` before constructing each action payload. <br>


## Reference(s): <br>
- [Gem homepage](https://www.gem.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-gem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before sending JSON payloads and returns connector responses as JSON.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
