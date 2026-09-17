## Description:

Raindrop.io support for reading, creating, updating, searching, and deleting bookmarks and collections through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage Raindrop.io bookmarks, collections, tags, and user profile data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include curl-to-bash and PowerShell online installer commands for the oo CLI.

Mitigation: Use a verifiable installation method where possible and do not allow the agent to run online installer commands automatically.

Risk: The skill can create, update, and delete Raindrop.io bookmarks and collections.

Mitigation: Require explicit user confirmation of the exact target, payload, and expected effect before write or destructive actions.

Risk: The skill depends on a third-party publisher and the oo CLI for account-connected Raindrop.io operations.

Mitigation: Install and use the skill only when OOMOL and the oo CLI are trusted for the target account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-raindrop)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Raindrop.io](https://raindrop.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before actions and may return oo CLI JSON responses.]

## Skill Version(s):

1.0.2 (source: metadata.version and release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
