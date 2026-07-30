## Description: <br>
Use this skill for Okta requests that read, create, update, or delete data through the OOMOL Okta connector instead of calling the API directly. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and identity administrators use this skill to inspect and manage Okta users and groups through an OOMOL-connected account. It supports read operations, user and group changes, and lifecycle actions that can affect identity access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact Okta identity administration actions. <br>
Mitigation: Install it only for agents expected to administer Okta, and require explicit approval before any user, group, credential, or lifecycle change. <br>
Risk: The lifecycle_user action can change account state but is not tagged as write or destructive in the skill text. <br>
Mitigation: Treat lifecycle_user as a state-changing action and confirm the exact target, requested lifecycle operation, and expected effect before execution. <br>


## Reference(s): <br>
- [Okta homepage](https://www.okta.com/) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-okta) <br>
- [Publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands call the OOMOL oo CLI and return JSON responses from the Okta connector.] <br>

## Skill Version(s): <br>
1.0.0 (source: skill frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
