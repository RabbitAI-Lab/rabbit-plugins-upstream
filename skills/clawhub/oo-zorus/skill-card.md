## Description:

Zorus connector skill for reading, creating, and updating Zorus data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations teams use this skill to search Zorus customers, endpoints, groups, policies, and active unblock requests. Agents use it to inspect live connector schemas and run Zorus actions through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the oo CLI.

Mitigation: Do not let an agent run the installer automatically; manually install a verified, versioned oo CLI release.

Risk: Some Zorus connector actions can change service state.

Mitigation: Review each action's live schema and effect, then require explicit user confirmation before any state-changing request.

## Reference(s):

- [ClawHub Zorus skill](https://clawhub.ai/oomol/skills/oo-zorus)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Zorus homepage](https://www.zorustech.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects returned by the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
