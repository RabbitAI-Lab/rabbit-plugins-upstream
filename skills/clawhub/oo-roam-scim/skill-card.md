## Description: <br>
Roam SCIM lets an agent read, create, update, and delete Roam SCIM users and groups through the OOMOL oo CLI instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to administer Roam SCIM through an OOMOL-connected account, including user lifecycle operations, group management, and service provider configuration lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or archive Roam SCIM users and groups through the connected OOMOL account. <br>
Mitigation: Require explicit user approval of the exact target, payload, and expected effect before running write or destructive actions. <br>
Risk: Full replacement actions can overwrite supported user attributes or group member lists. <br>
Mitigation: Fetch the live action schema first and review replacement payloads carefully before execution. <br>
Risk: The skill depends on the user's OOMOL authentication, service connection, scopes, and billing state. <br>
Mitigation: Only run setup, reconnection, or billing guidance after the oo command reports the corresponding error. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-roam-scim) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>
- [Roam SCIM Homepage](https://ro.am) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with oo CLI commands and JSON payload or response details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schemas before building action payloads.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
