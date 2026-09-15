## Description:

Gist lets an agent read, create, update, delete, fork, star, and manage GitHub Gists through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to manage GitHub Gists from an agent through an OOMOL-connected account, including read, write, comment, star, fork, and delete workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Gist access is delegated through an OOMOL connector with unclear permissions.

Mitigation: Install only after reviewing the connector permissions and use an account or scope appropriate for the intended Gist operations.

Risk: The setup instructions include remote installer commands that pipe network content into a shell.

Mitigation: Prefer a pinned, signed, or package-manager installation path, or independently verify the installer source before use.

Risk: Write and destructive Gist actions can modify or delete user content.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub Gist skill page](https://clawhub.ai/oomol/skills/oo-gist)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Gist homepage](https://gist.github.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and may return JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.3 (source: skill metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
