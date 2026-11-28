## Description:

Manage environment variables, secrets, and config across agent sessions. Secure credential storage with encryption at rest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[imaflytok](https://clawhub.ai/user/imaflytok)

### License/Terms of Use:


## Use Case:

Developers and agent operators use this skill to manage environment variables, API keys, and environment profiles across agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles credentials and claims encrypted secret storage without evidence of a vetted secret manager or keychain.

Mitigation: Use a vetted secret manager or OS keychain for production secrets, restrict file permissions, and review storage and loading behavior before installing.

Risk: The AGENTS.md or heartbeat sourcing instruction could persistently load untrusted configuration into agent sessions.

Mitigation: Scope auto-loading to trusted profiles, require trusted file ownership and restrictive permissions, and avoid enabling it globally.

Risk: External ClawSwarm links and hidden endpoint metadata are under-disclosed and untrusted.

Mitigation: Treat those endpoints as untrusted unless independently verified, and do not transmit secrets to them by default.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/imaflytok/skills/env-manager)
- [ClawSwarm multi-agent secrets link](https://onlyflies.buzz/clawswarm/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with bash commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Credential-handling guidance requires security review before production use.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
